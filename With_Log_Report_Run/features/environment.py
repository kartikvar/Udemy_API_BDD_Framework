def before_all(context):
    print("This is before all")

def before_feature(context, feature):
    print("This is before feature")

def before_scenario(context, scenario):
    print("This is before scenario")

def before_step(context, step):
    print("This is before step")

def after_step(context, step):
    print("This is after step")

def after_scenario(context, scenario):
    print("This is after scenario")

def after_feature(context, feature):
    print("This is after feature")

def after_all(context):
    print("This is after all")