import allure
from playwright.sync_api import Playwright, Page
from config import settings, Browser
from pathlib import Path
import time


def initialize_playwright_page(
        playwright: Playwright,
        test_name: str,
        browser_type: Browser,
        storage_state: str | None = None
) -> Page:
    browser = playwright[browser_type].launch(headless=settings.headless)
    context = browser.new_context(
        base_url=settings.get_base_url(),
        storage_state=storage_state,
        record_video_dir=settings.videos_dir
    )
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    video = page.video

    yield page

    context.tracing.stop(path=settings.tracing_dir.joinpath(f'{test_name}.zip'))
    allure.attach.file(settings.tracing_dir.joinpath(f'{test_name}.zip'), name='trace', extension='zip')
    browser.close()
    # Видео файл финализируется только после закрытия страницы/контекста.
    page.close()
    context.close()
    if video is not None:
        video_path = Path(video.path())
        timeout_sec = 3.0
        poll_interval_sec = 0.2
        deadline = time.time() + timeout_sec
        while time.time() < deadline:
            try:
                if video_path.exists() and video_path.stat().st_size > 0:
                    break
            except OSError:
                pass
            time.sleep(poll_interval_sec)

        if video_path.exists() and video_path.stat().st_size > 0:
            allure.attach.file(video_path, name='video', attachment_type=allure.attachment_type.WEBM)
