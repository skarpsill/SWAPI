---
title: "Face::GetShellType"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Face/Face__GetShellType.htm"
---

# Face::GetShellType

This
method is obsolete and has been superseded by[Face2::GetShellType](sldworksAPI.chm::/Face2/Face2__GetShellType.htm).

Description

Thismethodgets the shell type (open, internal, external) for this face.

Syntax (OLE Automation)

retval = Face.GetShellType ( )

(Table)=========================================================

| Return: | (int) retval | Shell type: 0 = An open shell.
For example, a face belonging to a sheet body or reference surface. 1 = An internal
shell. For example, a face which belongs to a cavity. Face helps define
an internal volume. 2 = An external
shell. For example, a typical face on a solid body (ie: helps "hold
in" the body mass). This would include all external faces including
faces belonging to bosses, pockets, holes, etc. |
| --- | --- | --- |

Syntax (COM)

status = Face->GetShellType ( &retval )

(Table)=========================================================

| Output: | (int) retval | Shell type: 0 = An open shell.
For example, a face belonging to a sheet body or reference surface. 1 = An internal
shell. For example, a face which belongs to a cavity. Face helps define
an internal volume. 2 = An external
shell. For example, a typical face on a solid body (ie: helps "hold
in" the body mass). This would include all external faces including
faces belonging to bosses, pockets, holes, etc. |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful; S_FALSE otherwise |

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
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Face_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="" >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\Face\Face__GetShellType.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
