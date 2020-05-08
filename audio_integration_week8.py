    text_clip_list = []
    audio_clip_list = []
    silence = mp.AudioFileClip('./audio/silence.mp3').subclip(0, 0.1)
    audio_clip_list.append(silence)
    for i in range(0, len(text_sentences)):
        sent_audio_clip = mp.AudioFileClip(audio_dir + '/' + str(i) + '.mp3')
        print("length of audio: " + str(i) + " = ", sent_audio_clip.duration)
        audio_clip_list.append(sent_audio_clip)
        sent_txt_clip = mp.TextClip(format_text(text_sentences[i]), font='Courier-Bold', fontsize=200, color='yellow', bg_color='black', stroke_width=30).set_pos('bottom').set_duration(sent_audio_clip.duration).resize(width=1000)
        text_clip_list.append(sent_txt_clip)

    audio_clip = mp.concatenate_audioclips(audio_clip_list)
