def df_to_number(data):
    df = data.copy()
    mode_dict = {'Major' : 1, 'Minor' : 0}
    key_dict = {'C' : 1, 'C#' : 2, 'D' : 3, 'D#' : 4, 'E' : 5, 'F' : 6, 
            'F#' : 7, 'G' : 8, 'G#' : 9, 'A' : 10, 'A#' : 11, 'B' : 12}

    df['time_signature'] = df['time_signature'].apply(lambda x : int(x[0]))
    df['mode'].replace(mode_dict, inplace=True)
    df['key'] = df['key'].replace(key_dict).astype(int)
    return df 