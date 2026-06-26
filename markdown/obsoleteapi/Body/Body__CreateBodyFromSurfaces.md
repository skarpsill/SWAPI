---
title: "Body::CreateBodyFromSurfaces"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__CreateBodyFromSurfaces.htm"
---

# Body::CreateBodyFromSurfaces

This method is obsolete and has been superseded by[Body2::CreateBodyFromSurfaces](sldworksAPI.chm::/Body2/Body2__CreateBodyFromSurfaces.htm).

Description

This method creates a body from a list of trimmed surfaces assumed to
have been already created.

Syntax (OLE Automation)

retval
= Body.CreateBodyFromSurfaces ()

(Table)=========================================================

| Return: | (BOOL)
retval | TRUE
if body creation is successful, FALSE if not |
| --- | --- | --- |

Syntax (COM)

status
= Body->CreateBodyFromSurfaces ( &retval )

(Table)=========================================================

| Output: | (VARIANT_BOOL)
retval | TRUE
if body creation is successful, FALSE if not |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK
if successful |

Remarks

This method is the final call to a set of related functions that are
designed to construct a body from trimmed surfaces. The first call in
this process is to PartDoc::CreateNewBody, which arranges for a place-holder
for all the trimmed surfaces.

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
<param name="Items" value="Body_Object$$**$$ZCreateSurface$$**$$ZCreateTemporaryBody$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\Body\Body__CreateBodyFromSurfaces.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
