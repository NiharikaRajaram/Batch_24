txt_clip = mp.concatenate_videoclips(text_clip_list).set_position('bottom')
   if len(title_clip_list) > 0:
       title_clip = mp.concatenate_videoclips(title_clip_list).set_position('top')
       result = mp.CompositeVideoClip([video_clip, txt_clip, title_clip])
   else:
       result = mp.CompositeVideoClip([video_clip, txt_clip])

   print("Composite video clip size: ", result.size)

   result_with_audio = result.set_audio(audio_clip)

   print("audio duration: " + str(audio_clip.duration))
   print("result duration: " + str(result.duration))
   print("result audio duration: " + str(result_with_audio.duration))

   result_with_audio.write_videofile(str(count_lines)+'.mp4', codec='libx264', fps=_FPS)
   count_lines += 1
