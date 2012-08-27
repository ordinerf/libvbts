from distutils.core import setup, Extension

setup(name="libvbts",
      version="0.0.1", 
      description="VBTS Tools for supporting community networks",
      author="Kurtis Heimerl",
      author_email="kheimerl@cs.berkeley.edu",
      url="http://tier.cs.berkeley.edu",
      packages=["libvbts"],
      license='BSD',
      scripts=[],
      install_requires=['python-messaging'],
      data_files=[
        ("/usr/local/share/yate/scripts/",['yate/VBTS_SMS_Route.py', 
                                           'yate/VBTS_SMS_Send.py',
                                           'yate/VBTS_SMS_Provisioning.py',
                                           'yate/VBTS_Route_Local.py',
                                           'yate/VBTS_Route_Provisioning.py',
                                           'yate/VBTS_Call_Originate.py',
                                           'yate/VBTS_Call_Provisioning.py',
                                           'yate/VBTS_SMS_Echo.py']),
        ("/usr/local/share/yate/sounds/", ['sounds/intro.gsm',
                                           'sounds/prompt.gsm',
                                           'sounds/error.gsm',
                                           'sounds/chosen.gsm',
                                           'sounds/chosen2.gsm',
                                           'sounds/invalid.gsm',
                                           'sounds/taken.gsm',
                                           'sounds/exit.gsm',
                                           'sounds/one.gsm',
                                           'sounds/two.gsm',
                                           'sounds/three.gsm',
                                           'sounds/four.gsm',
                                           'sounds/five.gsm',
                                           'sounds/six.gsm',
                                           'sounds/seven.gsm',
                                           'sounds/eight.gsm',
                                           'sounds/nine.gsm',
                                           'sounds/zero.gsm'])
        ]
      )
