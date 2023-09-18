from plyer import notification

notification_title = "TRUST THE PROCESS AND ENJOY EVERY DIFFICULTY"
notification_message = "Life won't be OK all the time. But remember, every night has a dawn. Try to enjoy every day of your life!"

notification.notify(
    title=notification_title,
    message=notification_message,
    app_icon="enes.ico",
    timeout=10,
    toast=False
)
