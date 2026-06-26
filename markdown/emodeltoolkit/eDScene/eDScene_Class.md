---
title: "eDScene Class"
project: ""
interface: "eDScene"
member: ""
kind: "class"
source: "emodeltoolkit/eDScene/eDScene_Class.htm"
---

# eDScene Class

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

A scene can represent an eDrawings document (.eprt,.easm, or.edrwfile) and contains:

- either one or more configurations or a single
  drawing.
- the methods to create bodies, textures, and the
  functionality to save the scene to disk as a.eprt,.easm, or.edrwfile.

#### Header file code

class eDScene :[eDObject](../eDObject/eDObject_Class.htm)

{

public:

eDOutcomebegin!kadov{{}}end!kadovCreateBody( const[eDAppearance](../eDAppearance/eDAppearance_Class.htm)&appearance,[eBody](../eDBody/eDBody_Class.htm)*& body ); //Creates a body

eDOutcomebegin!kadov{{}}end!kadovCreateConfiguration( constECHARbegin!kadov{{}}end!kadov*configname, const eDImage &thumbnail,[eDConfiguration](../eDConfiguration/eDConfiguration_Class.htm)*& configuration ); //Creates a configuration

eDOutcomebegin!kadov{{}}end!kadovCreateDrawing([eDDrawing](../eDDrawing/eDDrawing_Class.htm)*& drawing
); //Creates a drawing

eDOutcomebegin!kadov{{}}end!kadovCreateTexture( const[eDImageByRef](../eDImageByRef/eDImageByRef_Class.htm)&image,[eDParameterizationType](../Enumerators/eDParameterizationType.htm)texturetype,
BOOL blended,[eDTexture](../eDTexture/eDTexture_Class.htm)*& texture
); //Creates a texture

eDOutcomebegin!kadov{{}}end!kadovCreateSerializer([eDSerializer](../eDSerializer/eDSerializer_Class.htm)*&
serializer ); //Creates the eDSerializer object

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
<param name="Items" value="DocumentStructureClasses$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\eModelToolkit\eDScene\eDScene_Class.htm" >
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
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ZGeteDScene$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\eModelToolkit\eDScene\eDScene_Class.htm" >
<param name="_ID" value="RelatedTopic2" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>

Metadata type="DesignerControl" endspan
