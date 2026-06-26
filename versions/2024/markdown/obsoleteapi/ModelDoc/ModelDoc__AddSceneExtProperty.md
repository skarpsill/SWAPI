---
title: "ModelDoc::AddSceneExtProperty"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__AddSceneExtProperty.htm"
---

# ModelDoc::AddSceneExtProperty

This
property is obsolete and has been superseded by[ModelDoc2::AddSceneExtProperty](sldworksAPI.chm::/ModelDoc2/ModelDoc2__AddSceneExtProperty.htm).

Description

This method stores a float, string, or integer value for a scene. This
scene extension property is stored on the model document, but is unique
to the model's scene. To add the extension property, you must first define
the VARIANT type (float, string, or integer), give your variable a value,
and then call this method to place the value on the light source for future
reference.

Syntax (OLE Automation)

retval = ModelDoc.AddSceneExtProperty
( PropertyExtension)

(Table)=========================================================

| Input: | (VARIANT) PropertyExtension | Value you wish to store for the scene |
| --- | --- | --- |
| Return: | (long) retval | Unique identifier returned to allow you to access the Property Extension
in the future |

Syntax (COM)

status = ModelDoc->AddSceneExtProperty
( PropertyExtension, &retval )

(Table)=========================================================

| Input: | (VARIANT) PropertyExtension | Value you wish to store for the scene |
| --- | --- | --- |
| Output: | (long) retval | Unique identifier returned to allow you to access the Property Extension
in the future |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1323" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\ModelDoc\ModelDoc__AddSceneExtProperty.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
