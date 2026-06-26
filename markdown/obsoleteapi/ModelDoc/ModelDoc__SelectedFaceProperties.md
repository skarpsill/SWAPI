---
title: "ModelDoc::SelectedFaceProperties"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SelectedFaceProperties.htm"
---

# ModelDoc::SelectedFaceProperties

This method is obsolete
and has been superseded by[ModelDoc2::SelectedFaceProperties](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SelectedFaceProperties.htm).

Description

This method sets the property values of the selected face.

Syntax (OLE Automation)

retval = ModelDoc.SelectedFaceProperties
( rgbColor, ambient, diffuse, specular, shininess, transparency, emission,
usePartProps, faceName)

(Table)=========================================================

| Input: | (long) rgbColor | Face color |
| --- | --- | --- |
| Input: | (double) ambient | Face ambient value; valid range is from 0 to 1 |
| Input: | (double) diffuse | Face diffuse value; valid range is from 0 to 1 |
| Input: | (double) specular | Face specular value; valid range is from 0 to 1 |
| Input: | (double) shininess | Face shininess value; valid range is from 0 to 1 |
| Input: | (double) transparency | Face transparency value; valid range is from 0 to 1 |
| Input: | (double) emission | Face emission value; valid range is from 0 to 1 |
| Input: | (BOOL) usePartProps | TRUE if the face will inherit the Part properties, FALSE otherwise |
| Input: | (BSTR) faceName | Name of the face |
| Return: | (BOOL) retval | TRUE if successfully changed the face properties, FALSE otherwise |

Syntax (COM)

status = ModelDoc->SelectedFaceProperties
( rgbColor, ambient, diffuse, specular, shininess, transparency, emission,
usePartProps, faceName, &retval )

(Table)=========================================================

| Input: | (long) rgbColor | Face color |
| --- | --- | --- |
| Input: | (double) ambient | Face ambient value;valid range is from 0 to 1 |
| Input: | (double) diffuse | Face diffuse value; valid range is from 0 to 1 |
| Input: | (double) specular | Face specular value; valid range is from 0 to 1 |
| Input: | (double) shininess | Face shininess value; valid range is from 0 to 1 |
| Input: | (double) transparency | Face transparency value; valid range is from 0 to 1 |
| Input: | (double) emission | Face emission value; valid range is from 0 to 1 |
| Input: | (VARIANT_BOOL) usePartProps | TRUE if the face will inherit the Part properties, FALSE otherwise |
| Input: | (BSTR) faceName | Name of the face |
| Output: | (VARIANT_BOOL) retval | TRUE if successfully changed the face properties, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The faceName argument allows you to set the name for this face. If this
face does not already have a name, then this method sets the name.

If the face already has a name, then this method does not change the
name and returns FALSE. This behavior is intended to prevent a program
from renaming an face that is referenced in some other location.

For example, if an assembly contains a mate to an face on a part, then
SolidWorks automatically assigns a name to that face. If you change that
name, then there is no guarantee that the mate will still be valid. Therefore,
when using entity names, you should first check to see if the entity is
already named, and if so, use the existing name. If no name exists for
the face, then you can give the face a name.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0
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
<param name="Items" value="ModelDoc_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__SelectedFaceProperties.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
