---
title: "Face::MaterialUserName"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Face/Face__MaterialUserName.htm"
---

# Face::MaterialUserName

This
method is obsolete and has been superseded by[Face2::MaterialUserName](sldworksAPI.chm::/Face2/Face2__MaterialUserName.htm).

Description

This property gets or sets the material name, which is visible to the
user.

Syntax (OLE Automation)

name
= Face.MaterialUserName (VB Get property)

Face.MaterialUserName
= name (VB Set property)

name
= Face.GetMaterialUserName ( ) (C++ Get property)

Face.SetMaterialUserName
( name ) (C++ Set property)

(Table)=========================================================

| Property: | (BSTR)
name | Material
user name property on the individual face |
| --- | --- | --- |

Syntax (COM)

status
= Face-> get_MaterialUserName( &name )

status
= Face-> put_MaterialUserName( name )

(Table)=========================================================

| Property: | (BSTR)
name | Material
user name property on the individual face |
| --- | --- | --- |
| Return: | (HRESULT)
status | S_OK
if successful |

Remarks

This property is unsupported for faces obtained from reference surface
bodies.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1323" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Face_Object$$**$$ZGetNames$$**$$ZModifyNames$$**$$ZGetInfoFace$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="" >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\Face\Face__MaterialUserName.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
