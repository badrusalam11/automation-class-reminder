def before_scenario(context, scenario):
    print(f"Starting scenario: {scenario.name}")

def after_scenario(context, scenario):
    if context.driver:
        context.driver.quit()
    print(f"Scenario finished: {scenario.name}")
