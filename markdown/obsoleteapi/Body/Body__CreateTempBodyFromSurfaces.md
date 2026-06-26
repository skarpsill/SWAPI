---
title: "Body::CreateTempBodyFromSurfaces"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__CreateTempBodyFromSurfaces.htm"
---

# Body::CreateTempBodyFromSurfaces

This
method is obsolete and has been superseded by[Body2::CreateTempBodyFromSurfaces](sldworksAPI.chm::/Body2/Body2__CreateTempBodyFromSurfaces.htm).

Description

This method creates a body from a list of existing trimmed surfaces.

Syntax (OLE Automation)

retval
= Body.CreateTempBodyFromSurfaces ( )

(Table)=========================================================

| Return: | (LPDISPATCH)
retval | Pointer
to a dispatch object, the body |
| --- | --- | --- |

Syntax (COM)

status
= Body->ICreateTempBodyFromSurfaces ( &retval )

(Table)=========================================================

| Output: | (LPBODY)
retval | Pointer
to the temporary body |
| --- | --- | --- |
| Return: | (HRESULT)
status | S_OK
if successful |

Remarks

This method is the last in a set of related methods (like Body::CreateBodyFromSurfaces)
that construct a temporary body from trimmed surfaces. The first method
you need to call in this process is PartDoc::CreateNewBody, which arranges
for a place-holder for all the trimmed surfaces.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Body_Object$$**$$ZCreateTemporaryBody$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\Body\Body__CreateTempBodyFromSurfaces.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
