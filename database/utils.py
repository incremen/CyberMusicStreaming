def log_user_and_playlists(session, user_id):
    user = session.query(User).filter_by(id=user_id).first()
    print(f"User: {user.username}")
    for playlist in user.playlists:
        print(f"Playlist ID: {playlist.id}, Items: {playlist.items}")
