---
title: "eDSerializerParams Class"
project: ""
interface: "eDSerializerParams"
member: ""
kind: "class"
source: "emodeltoolkit/eDSerializerParams/eDSerializerParams_Class.htm"
---

# eDSerializerParams Class

(Generated Script Links)========================================

(Generated Code)================================================

(WARNING: DO NOT EDIT OR DELETE THIS SECTION!)==================

begin!kadov{{===================================================

}}end!kadov=====================================================

(==============================================================)

(Table)=========================================================

| See
Also | Example | Accessors | Availability |
| --- | --- | --- | --- |

Contains options for saving eDrawings documents to disk.

NOTE:Unicode filenames are
not supported. To create a Unicode filename, first create a filename with
ANSI characters and then rename it.

#### Header file code

class eDSerializerParams

{

public:

eDSerializerParams(

constECHARbegin!kadov{{}}end!kadov* filename,

const[eDImage](../eDImageByRef/eDImageByRef_Class.htm)* previewImage //Preview image or a NULL pointer

BOOL compress,

BOOL rotateenabled,

BOOL reviewenabled,

BOOL measureenabled,

BOOL simplifiedui,

BOOL stlexportenabled,

BOOL shadingenabled,

BOOL isexploded,

eDUnitsTypebegin!kadov{{}}end!kadovunits, //All units are in meters; this parameter only sets the default
unit for when a model is opened in the eDrawings viewer. For example,
if you want to describe a model in inches, you must, in your publisher
program, convert your values to meters, e.g., 1 inch = .0254 meters, and
then set the this parameter to eDUnitInches. That way, inches will be
the default unit type that appears when the model is measured in eDrawings.
Then, the values you multiplied by .0254 to convert to meters will by
multiplied back by 1/.0254 to display inches. All units are in meters.

eDDisplayTypebegin!kadov{{}}end!kadovdisplay,

eDDocumentTypebegin!kadov{{}}end!kadovdocumenttype,

[eDTransform3d](../eDTransform3d/eDTransform3d_Class.htm)viewtransform,

[eDColorRGB](../eDColorRBG/eDColorRBG_Class.htm)backgroundcolor,

[eDColorRGB](../eDColorRBG/eDColorRBG_Class.htm)papercolor,

[eDTime](../eDTime/eDTime_Class.htm)expiredate,

constECHARbegin!kadov{{}}end!kadov* password = NULL,

[eDConfiguration](../eDConfiguration/eDConfiguration_Class.htm)* activeconfiguration = NULL ); //Specifies options for saving eDrawings
document to disk

[eDCamera](../eDCamera/eDCamera_Class.htm)initialcamera =[eDCamera](../eDCamera/eDCamera_Class.htm)()
//if initialcamera is specified, viewtransform is ignored

);

};

kadov_tag{{<implicit_p>}}

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic1
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="DocumentStructureClasses$$**$$eDSerializer$$**$$e" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\eModelToolkit\eDSerializerParams\eDSerializerParams_Class.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>

Metadata type="DesignerControl" endspan

begin!kadov{{

}}end!kadov

kadov_tag{{<implicit_p>}}

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic2
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ZGeteDSerializerParams$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\eModelToolkit\eDSerializerParams\eDSerializerParams_Class.htm" >
<param name="_ID" value="RelatedTopic2" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>

Metadata type="DesignerControl" endspan
