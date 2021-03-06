<?php

// autoload_static.php @generated by Composer

namespace Composer\Autoload;

class ComposerStaticInit766ef181273e88079c2d5534e17fa265
{
    public static $prefixLengthsPsr4 = array (
        'M' => 
        array (
            'Michelf\\' => 8,
        ),
    );

    public static $prefixDirsPsr4 = array (
        'Michelf\\' => 
        array (
            0 => __DIR__ . '/..' . '/michelf/php-markdown/Michelf',
        ),
    );

    public static function getInitializer(ClassLoader $loader)
    {
        return \Closure::bind(function () use ($loader) {
            $loader->prefixLengthsPsr4 = ComposerStaticInit766ef181273e88079c2d5534e17fa265::$prefixLengthsPsr4;
            $loader->prefixDirsPsr4 = ComposerStaticInit766ef181273e88079c2d5534e17fa265::$prefixDirsPsr4;

        }, null, ClassLoader::class);
    }
}
