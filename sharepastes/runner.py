import optparse
import xerox

from sharepastes.core import SharePastesFactory


def main():
    parser = optparse.OptionParser()
    using_help = '''
    the service that you want to use. For example: gist for Github's Gist,
    pastebin for PasteBin.com
    '''
    parser.add_option('-u', '--using', dest='using',
                      help=using_help)

    (options, args) = parser.parse_args()

    using = options.using
    if not using:
        using = 'pastebin'

    obj = SharePastesFactory.create(using)
    try:
        url = obj.api_call(xerox.paste())
        xerox.copy(url)
    except xerox.base.XclipNotFound:
        print 'xclip not found. Install xclip for SharePastes to work.'
        sys.exit(1)

    try:
        from pync import Notifier
        Notifier.notify('URL added to your clipboard %s.' % url,
                        title='SharePastes')
    except:
        pass


if __name__ == '__main__':
    main()
