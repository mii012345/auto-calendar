from get_data import Channel

def main():
    channel = Channel()
    kafu = 'UCQ1U65-CQdIoZ2_NA4Z4F7A'
    kafu_video = channel.get_preserve_video(kafu)
    print(kafu_video)


if __name__ == '__main__':
    main()