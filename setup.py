from setuptools import setup

setup(
    name='fast_pub',
    version="0.1",
    description="异步行情交易处理中心",
    author='somewheve',
    long_description="高性能行情网关",
    author_email='somewheve@gmail.com',
    url='https://github.com/ctpbee/fast-pub',
    license="MIT",
    packages=[],
    install_requires=["ctpbee", "fastapi", "uvicorn"],
    platforms=["Windows", "Linux", "Mac OS-X"],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
