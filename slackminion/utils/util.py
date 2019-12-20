import textwrap
import asyncio

def format_docstring(docstring):
    """
    Uses textwrap to auto-dedent a docstring (removes leading spaces)
    Returns the docstring in a pre-formatted block with required characters escaped.
    https://api.slack.com/docs/message-formatting
    :param docstring: str
    :return: str
    """
    if not docstring:
        return ''
    formatted_text = '```{}```'.format(
        textwrap.dedent(docstring.replace('&', '&amp;')
                        .replace('<', '&lt;')
                        .replace('>', '&gt;')
                        )
    )
    return formatted_text


async def dev_mode_repl(bot):
    banner = 'Slackminion: Starting DEV MODE'
    if hasattr(bot, 'user_manager'):
        delattr(bot, 'user_manager')
    while not bot.webserver.thread.is_alive:
        print('Waiting for webserver to start...')
        await asyncio.sleep(1)
    print(banner)
    print('=' * len(banner))
    while bot.runnable:
        try:
            command = input("Slackminion DEV_MODE (type a !command.  use 'exit' to leave)> ")
            if command.lower() in ['quit', 'exit']:
                bot.runnable = False
                continue
            elif len(command) == 0:
                continue
        except (KeyboardInterrupt, EOFError) as e:
            bot.log.exception('Caught {}'.format(e))
            bot.runnable = False
            raise

        print(f'read command: {command}')
        payload = {
            'data': {
                'user': 'console_user',
                'channel': 'test channel',
                'text': command,
                'ts': None
            }
        }
        await bot._event_message(**payload)
