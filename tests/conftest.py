import pytest
import os


@pytest.fixture
def browser(context, request):
    page = context.new_page()
    if request.node.execution_count == 2:
        context.tracing.start(screenshots=True, snapshots=True)

    yield page
    if request.node.execution_count == 2 and request.node.rep_call.passed == False:
        path_to_res = f"./output/{request.node.name}"
        try:
            os.makedirs(path_to_res)
        except FileExistsError:
            pass
        page.screenshot(path=f"{path_to_res}/screenshot.png")
        context.tracing.stop(path = f"{path_to_res}/trace.zip")
    page.close()
    context.close()



