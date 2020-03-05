fr = open('clean.txt')
count_lines = 1
for line in fr:
    line = line.replace('\n','')
    all_topics = get_topics_from_text1(line)
    print '\n\n',line,'\n'
    print "all topics ", all_topics, '\n\n'


    text_sentences=[f for f in line.split('.') if len(f)>1]

    if not os.path.exists(audio_dir):
    	os.mkdir(audio_dir)
    if not os.path.exists(picture_dir):
    	os.mkdir(picture_dir)
    if not os.path.exists(video_dir):
    	os.mkdir(video_dir)

    print "creating "+str(len(text_sentences))+" audio files "
    for i in range(0,len(text_sentences)):
    	tts = gTTS(text=text_sentences[i], lang='en', slow=False)
    	tts.save(audio_dir+'/'+str(i)+'.mp3')
        print '\n',text_sentences[i],'\n'
        print "created "+ str(i)+ " audio file"
