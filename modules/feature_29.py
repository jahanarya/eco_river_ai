# Feature 29.py implementation here
def feature_29_func(sound_file: str = "alert.wav") -> None:
    """
    Play an emergency alert sound.
    Args:
        sound_file: Path to sound file
    Returns:
        None
    """
    try:
        import simpleaudio as sa
        wave_obj = sa.WaveObject.from_wave_file(sound_file)
        play_obj = wave_obj.play()
        play_obj.wait_done()
    except Exception as e:
        print(f"Cannot play sound: {e}")