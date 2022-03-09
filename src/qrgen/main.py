import click
import qrcode
from qrcode.image.pil import PilImage


@click.command(name='qrgen')
@click.version_option()
@click.option(
    '-s',
    '--ssid',
    type=str,
    help='The name of the wifi network',
    prompt=True,
)
@click.password_option('-k', '--keyphrase', confirmation_prompt=False)
@click.option(
    '--wpa',
    'security_type',
    help='Use WPA as the security type. This is the default behaviour',
    flag_value='WPA',
    default=True
)
@click.option(
    '--wep',
    'security_type',
    help='Use WEP as the security type.',
    flag_value='WEP',
)
@click.option(
    '--ascii',
    'is_ascii',
    is_flag=True,
    help='Print the QR code in ASCII to the terminal',
)
@click.option(
    '-o',
    '--output',
    help='The name of the output file for the QR code',
    default='wifi.png',
    show_default=True,
    type=str,
)
@click.option(
    '--no-save',
    'should_save',
    help='Prevent file from being saved',
    default=True,
    is_flag=True,
)
def main(
    ssid: str,
    keyphrase: str,
    security_type: str,
    output: str,
    is_ascii: bool,
    should_save: bool,
):
    wifi_string = f'WIFI:T:{security_type};S:{ssid};P:{keyphrase};;'

    qr = qrcode.QRCode()

    qr.add_data(wifi_string)

    if is_ascii:
        qr.print_ascii()

    if should_save:
        img: PilImage = qr.make_image()

        img.save(output)



if __name__ == '__main__':  # pragma: no cover
    main()
