import munepy

__all__ = [
    'CompositeOp',
    'VirtualPixelMethod',
    'ChannelType',
    'FilterTypes',
    'ColorspaceType',
    ]

def enum_as_param(self):
    return int(self)

@classmethod
def enum_from_param(C, value):
    return int(value)

class CompositeOp(munepy.Enum):
    Undefined = 0
    No = 1
    Add = 2
    Atop = 3
    Blend = 4
    Bumpmap = 5
    ChangeMask = 6
    Clear = 7
    ColorBurn = 8
    ColorDodge = 9
    Colorize = 10
    CopyBlack = 11
    CopyBlue = 12
    Copy = 13
    CopyCyan = 14
    CopyGreen = 15
    CopyMagenta = 16
    CopyOpacity = 17
    CopyRed = 18
    CopyYellow = 19
    Darken = 20
    DstAtop = 21
    Dst = 22
    DstIn = 23
    DstOut = 24
    DstOver = 25
    Difference = 26
    Displace = 27
    Dissolve = 28
    Exclusion = 29
    HardLight = 30
    Hue = 31
    In = 32
    Lighten = 33
    LinearLight = 34
    Luminize = 35
    Minus = 36
    Modulate = 37
    Multiply = 38
    Out = 39
    Over = 40
    Overlay = 41
    Plus = 42
    Replace = 43
    Saturate = 44
    Screen = 45
    SoftLight = 46
    SrcAtop = 47
    Src = 48
    SrcIn = 49
    SrcOut = 50
    SrcOver = 51
    Subtract = 52
    Threshold = 53
    Xor = 54
    Divide = 55

CompositeOp._as_param_ = property(enum_as_param) #hacks
CompositeOp.from_param = enum_from_param

class VirtualPixelMethod(munepy.Enum):
    Undefined = 0
    Background = 1
    Constant = 2 # deprecated
    Dither = 3
    Edge = 4
    Mirror = 5
    Random = 6
    Tile = 7
    Transparent = 8
    Mask = 9
    Black = 10
    Gray = 11
    White = 12

VirtualPixelMethod._as_param_ = property(enum_as_param) #hacks
VirtualPixelMethod.from_param = enum_from_param

class ChannelType(munepy.Enum):
    Undefined = 0
    Red = 0x0001
    Green = 0x0002
    Blue = 0x0004
    Alpha = 0x0008
    Black = 0x0020
    All = 0xff
    Defaults = (All &~ Alpha)

ChannelType._as_param_ = property(enum_as_param) #hacks
ChannelType.from_param = enum_from_param
# Aliases
ChannelType.Yellow = ChannelType.Blue
ChannelType.Opacity = ChannelType.Alpha
ChannelType.Matte = ChannelType.Alpha # deprecated
ChannelType.Index = ChannelType.Black
ChannelType.Magenta = ChannelType.Green
ChannelType.Cyan = ChannelType.Red
ChannelType.Gray = ChannelType.Red

class FilterTypes(munepy.Enum):
    UndefinedFilter = 0
    PointFilter = 1
    BoxFilter = 2
    TriangleFilter = 3
    HermiteFilter = 4
    HanningFilter = 5
    HammingFilter = 6
    BlackmanFilter = 7
    GaussianFilter = 8
    QuadraticFilter = 9
    CubicFilter = 10
    CatromFilter = 11
    MitchellFilter = 12
    LanczosFilter = 13
    BesselFilter = 14
    SincFilter = 15
    KaiserFilter = 16
    WelshFilter = 17
    ParzenFilter = 18
    LagrangeFilter = 19
    BohmanFilter = 20
    BartlettFilter = 21
    SentinelFilter = 22  # a count of all the filters, not a real filter

FilterTypes._as_param_ = property(enum_as_param) #hacks
FilterTypes.from_param = enum_from_param

class ColorspaceType(munepy.Enum):
    Undefined = 0
    RGB = 1
    GRAY = 2
    Transparent = 3
    OHTA = 4
    Lab = 5
    XYZ = 6
    YCbCr = 7
    YCC = 8
    YIQ = 9
    YPbPr = 10
    YUV = 11
    CMYK = 12
    sRGB = 13
    HSB = 14
    HSL = 15
    HWB = 16
    Rec601Luma = 17
    Rec601YCbCr = 18
    Rec709Luma = 19
    Rec709YCbCr = 20
    Log = 21
    CMY = 22

ColorspaceType._as_param_ = property(enum_as_param) #hacks
ColorspaceType.from_param = enum_from_param
