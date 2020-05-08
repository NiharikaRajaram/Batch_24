file_names = []
    for i in range(0, len(folder_names)):
        files = (fn for fn in os.listdir(picture_dir + '/' + folder_names[i]) if fn.endswith('.jpg') or fn.endswith('.png') or fn.endswith('.PNG') or fn.endswith('.JPG') or fn.endswith('.jpeg') or fn.endswith('.JPEG'))
        for file in files:
            file_names.append(folder_names[i] + '/' + file)

    # s_file_names = sorted(file_names, key=lambda x: x.split('.')[0].split('/')[1])
    s_file_names = file_names
    number_of_images = len(s_file_names)
    print("s_file_names")

    video_clip_list = []
    black_clip = mp.ImageClip('./downloads/black1.jpg').set_duration(0.1).set_fps(_FPS)
    video_clip_list.append(black_clip)
    black = './downloads/black1.jpg'
    title_clip_list = []
    if number_of_images > 0:
        for f in s_file_names:
            temp_clip = mp.ImageClip(picture_dir + '/' + f).set_duration(audio_clip.duration / number_of_images).set_position('center').set_fps(_FPS).crossfadein(0.5)
            name_txt_clip = mp.TextClip(format_text(' '.join([word[:1].upper() + word[1:] for word in f.split('/')[0].split('_')])),font='Courier-Bold', fontsize=200, color='yellow', bg_color='black', stroke_width=30).set_position('top').set_duration(audio_clip.duration / number_of_images).resize(height=30)
            title_clip_list.append(name_txt_clip)
            # temp_clip = CompositeVideoClip([temp1_clip,name_txt_clip])
            video_clip_list.append(temp_clip)
            # minimum_image_size=min([minimum_image_size,temp_clip.size[0]])
            print('temp_clip width: ', temp_clip.size)
    else:
        temp_clip = mp.ImageClip(black).set_duration(audio_clip.duration).set_fps(_FPS)
        video_clip_list.append(temp_clip)
        # minimum_image_size=min([minimum_image_size,temp_clip.size[0]])

    video_clip = mp.concatenate_videoclips(video_clip_list).set_position('center')
