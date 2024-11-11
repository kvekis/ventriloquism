# Ventriloquism 

Ventriloquism - это микропрограммка, примерно повторяющая функционал вебки(?) [Пугода](https://www.twitch.tv/pwgood)  
Ventriloquism is a microprogram that roughly replicates the functionality of [PWGood's](https://www.twitch.tv/pwgood) webcam(?)

## Содержание / Contents


- [Ventriloquism](#ventriloquism)
  - [Содержание / Contents](#содержание--contents)
  - [RU](#ru)
    - [Soundmeter](#soundmeter)
      - [Конфигурация](#конфигурация)
    - [Ventriloquism](#ventriloquism-1)
      - [Конфигурация](#конфигурация-1)
      - [Использование Soundmeter](#использование-soundmeter)
  - [EN](#en)
    - [Soundmeter](#soundmeter-1)
      - [Configuration](#configuration)
    - [Ventriloquism](#ventriloquism-2)
      - [Configuration](#configuration-1)
      - [Using Soundmeter](#using-soundmeter)

## RU

### Soundmeter
Эта нанопрограммка нужна для настройки основной. Она показывает уровень сигнала с микрофона. Из-за особенностей алгоритма `0` является максимальным значением
#### Конфигурация
У этой программки можно настроить только внешний вид.  
Файл конфигурации `soundmeter_config.json` находится в директории `config`  

`BackgroundColor` - цвет фона в формате HEX  
`Font` - шрифт, который программа будет использовать. Должен быть записан строчными буквами без пробелов  
`FontSize` - размер шрифта  
`FontColor` - цвет щрифта в формате HEX  
`Width` и `Height` - ширина и высота окна программы

### Ventriloquism
Сама микропрограммка, ради которой всё и затевалось. Она отображает изображения в зависимости от того, какой громкости поступает сигнал с микрофона
#### Конфигурация
У этой программки можно насторить и внешний вид, и поведение.  
Файл конфигурации `ventriloquism_config.json` находится в директории `config`

`FPS` - количество кадров/сек, отображаемых программой (хотя на самом деле будет отображаться совсем чуть-чуть меньше). Значения больше `30` могут сильно нагружать систему  
`BackgroundColor` - цвет фона онка в формате HEX. Лучше ставить более-менее контрастный цвет фона отонсительно ваших изображений, чтобы их было легче отделить  
`Width` и `Height` - ширина и высота окна программы  
`Images` - здесь хранится вся информация о каждом изображении в виде `"{ImageName}": ["{ImageParameters}", {MaxVolume}]` (без фигурных скобок). `{ImageName}` - название изображения. Изображение с таким названием в формате `.png` должно быть в директории `images`. `{ImageParameters}` - строка, содержащая параметры поведения соответствующего изображения. Если параметр `s` есть в этой строке, то изображение будет трястить при появлении. Если в этой строке есть параметр `b`, то изображение будет "моргать". Оно будет сменяться на некоторое время изображением с названием `{ImageName}_blink` в формате `.png`. `MaxVolume` - максимальная громкость сигнала микрофона, при которой булет появляться данное изображение. Изображения в `Images` должны идти строго по возрастанию этого параметра  
`ImageSize` - то, насколько будет масштабироваться изображение. Нужен для более удобного отделения изображения от фона и для лучшей видимости изображения при тряске  
`ShakePower` - сила тряски изображения в пикселях  
`VolumeDisplay` и `ShakeDisplay` - включение и отключение уведомлений(?) в терминале о громкости сигнала микрофона в данный момент и тряске  
`BlinkFrames` - количество кадров моргания  
`BlinkInterval` - время до следующего моргания (почему-то измеряется не в кадрах)  
`BlinkIntervalRandom` - максимальное отклонение времени до следующего моргания в обе стороны

#### Использование Soundmeter
С помощью Soundmeter вы можете настроить `MaxVolume`, чтобы изображения появлялись при нужной вам громкости



## EN

### Soundmeter
This nanoprogram is needed to set up the main one. It shows the signal strength from the microphone. Due to the peculiarities of the algorithm, `0` is the maximum value
#### Configuration
You can only customize the appearance of this program.  
The configuration file `soundmeter_config.json` is located in the `config` directory  

`backgroundColor` - the background color in HEX format  
`Font` - the font that the program will use. It must be written in lowercase letters without spaces  
`FontSize` - font size  
`FontColor` - the font color in HEX format  
`Width` and `Height` - width and height of the program window

### Ventriloquism
This program displays images depending on the volume of the microphone signal
#### Configuration
In this program, you can alert both the appearance and behavior.  
The configuration file `ventriloquism_config.json` is located in the `config` directory

`FPS`- the number of frames/sec displayed by the program (although in fact it will be displayed just a little less). Values greater than `30` can put a lot of strain on the system  
`backgroundColor` - the background color of the icon in HEX format. It is better to set contrasting background color relative to your images so that they are easier to separate  
`Width` and `Height` - width and height of the program window  
`Images` - all information about each image is stored here in the form of `"{ImageName}": ["{ImageParameters}", {MaxVolume}]` (without curly brackets). `{ImageName}` is the name of the image. Images with this name in the `.png` format should be in the `images` directory. `{ImageParameters}` is a string containing the behavior parameters of the image. If the `s` parameter is in this string, then the image will shake when it appears. If there is a `b` parameter in this string, then the image will "blink". It will be replaced for a while by an image with the name `{ImageName}_blink` in the format `.png`. `MaxVolume` - the maximum volume of the microphone signal at which this image will appear. The images in `Images` must go strictly in ascending order of this parameter  
`ImageSize` - how much the image will be scaled. It is needed for more convenient separation of the image from the background and for better visibility of the image when shaking  
`ShakePower` - the force of image shaking in pixels  
`VolumeDisplay` and `ShakeDisplay` - enable and disable notifications(?) in the terminal, about the volume of the microphone signal at the moment and the shaking  
`BlinkFrames` - the number of blink frames  
`BlinkInterval` - time until the next blink (for some reason it is not measured in frames)  
`BlinkIntervalRandom` - the maximum deviation of the time until the next blink in both directions

#### Using Soundmeter
With Soundmeter, you can adjust the `MaxVolume` so that the images appear at the volume you need.