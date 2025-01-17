
from Bot.plugins.database.mongo_db import check_crf_mdb,check_user_mdb,check_vcodec_settings,update_vcodec_settings,check_preset_settings,update_preset_settings,check_resolution_settings,check_audio_type_mdb, update_audio_type_mdb,update_resolution_settings

def ffmpeg_settings(id, input, FT):
    resolutio = check_resolution_settings(id)
    audio_type = check_audio_type_mdb(id)
    preset = check_preset_settings(id)
    vcodec = check_vcodec_settings(id)
    crf = check_crf_mdb(id)
    if crf is None:
        crf = 28
    output = input.rsplit('.',1)[0]
    if '.mkv' in input:
        output = output+'_IA.mkv'    
    else:
        output = output+'_IA.mp4'    
    
    if vcodec == 'x264':
        vcodecs = 'libx264'
    elif vcodec == 'x265':
        vcodecs = 'libx265'     
    
    if resolutio == '480p':
        resolution = '640x480'
    elif resolutio == '720p':
        resolution = '1280x720'   
    else:
        resolution = '1920x1080'  
    
    if audio_type == 'opus':
        if resolutio == '480p':
            cmd = f'ffmpeg -hide_banner -loglevel quiet -progress progress-{FT}.txt -i """{input}""" -preset {preset} -vcodec {vcodecs} -crf {crf} -s {resolution} -metadata title="Encoded By RAHAT" -metadata:s:v title="RAHAT - {resolutio} - {vcodec}"  -metadata:s:a title="RAHAT" -map 0:v -c:a opus -b:a 64k -map 0:a -c:s copy -map 0:s? -strict -2 """{output}""" -y'
        elif resolutio == '720p':
            cmd = f'ffmpeg -hide_banner -loglevel quiet -progress progress-{FT}.txt -i """{input}""" -preset {preset} -vcodec {vcodecs} -crf {crf} -s {resolution} -metadata title="Encoded By RAHAT" -metadata:s:v title="RAHAT - {resolutio} - {vcodec}"  -metadata:s:a title="RAHAT" -map 0:v -c:a opus -b:a 128k -map 0:a -c:s copy -map 0:s? -strict -2 """{output}""" -y'
        else:
            cmd = f'ffmpeg -hide_banner -loglevel quiet -progress progress-{FT}.txt -i """{input}""" -preset {preset} -vcodec {vcodecs} -crf {crf} -metadata title="Encoded By RAHAT" -metadata:s:v title="RAHAT - {resolutio} - {vcodec}"  -metadata:s:a title="RAHAT" -map 0:v -c:a opus -b:a 256k -map 0:a -c:s copy -map 0:s? -strict -2 """{output}""" -y'
    
    elif audio_type == 'aac':
        if resolutio == '480p':
            cmd = f'ffmpeg -hide_banner -loglevel quiet -progress progress-{FT}.txt -i """{input}""" -preset {preset} -vcodec {vcodecs} -crf {crf} -s {resolution} -metadata title="Encoded By RAHAT" -metadata:s:v title="RAHAT - {resolutio} - {vcodec}"  -metadata:s:a title="RAHAT" -map 0:v -c:a aac -b:a 64k -map 0:a -c:s copy -map 0:s? """{output}""" -y'
        elif resolutio == '720p':
            cmd = f'ffmpeg -hide_banner -loglevel quiet -progress progress-{FT}.txt -i """{input}""" -preset {preset} -vcodec {vcodecs} -crf {crf} -s {resolution} -metadata title="Encoded By RAHAT" -metadata:s:v title="RAHAT - {resolutio} - {vcodec}"  -metadata:s:a title="RAHAT" -map 0:v -c:a aac -b:a 128k -map 0:a -c:s copy -map 0:s? """{output}""" -y'
        else:
            cmd = f'ffmpeg -hide_banner -loglevel quiet -progress progress-{FT}.txt -i """{input}""" -preset {preset} -vcodec {vcodecs} -crf {crf} -metadata title="Encoded By RAHAT" -metadata:s:v title="RAHAT - {resolutio} - {vcodec}"  -metadata:s:a title="RAHAT" -map 0:v -c:a aac -b:a 256k -map 0:a -c:s copy -map 0:s? """{output}""" -y'
    
    elif audio_type == 'libopus':
        if resolutio == '480p':
            cmd = f'ffmpeg -hide_banner -loglevel quiet -progress progress-{FT}.txt -i """{input}""" -preset {preset} -vcodec {vcodecs} -crf {crf} -s {resolution} -metadata title="Encoded By RAHAT" -metadata:s:v title="RAHAT - {resolutio} - {vcodec}"  -metadata:s:a title="RAHAT" -map 0:v -c:a libopus -b:a 64k -map 0:a -c:s copy -map 0:s? """{output}""" -y'
        elif resolutio == '720p':
            cmd = f'ffmpeg -hide_banner -loglevel quiet -progress progress-{FT}.txt -i """{input}""" -preset {preset} -vcodec {vcodecs} -crf {crf} -s {resolution} -metadata title="Encoded By RAHAT" -metadata:s:v title="RAHAT - {resolutio} - {vcodec}"  -metadata:s:a title="RAHAT" -map 0:v -c:a libopus -b:a 128k -map 0:a -c:s copy -map 0:s? """{output}""" -y'
        else:
            cmd = f'ffmpeg -hide_banner -loglevel quiet -progress progress-{FT}.txt -i """{input}""" -preset {preset} -vcodec {vcodecs} -crf {crf} -metadata title="Encoded By RAHAT" -metadata:s:v title="RAHAT - {resolutio} - {vcodec}"  -metadata:s:a title="RAHAT" -map 0:v -c:a libopus -b:a 256k -map 0:a -c:s copy -map 0:s? """{output}""" -y'        
    return cmd      
        
