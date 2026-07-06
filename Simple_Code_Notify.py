import plyer
# print(plyer.__version__) # to check if installed or not we use this syntax mainly.
# plyer named module is used in prooducing the notify.

from plyer import notification as nf
nf.notify(
    title="My New Notification",
    message="Hey Rahul How Are You Bro!!!!!",
    app_icon=None,
    timeout=10,
    )
