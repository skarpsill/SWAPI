---
title: "Body::RemoveFacesFromSheet"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__RemoveFacesFromSheet.htm"
---

# Body::RemoveFacesFromSheet

This method is obsolete and has been superseded by[Body2::RemoveFacesFromSheet](sldworksAPI.chm::/Body2/Body2__RemoveFacesFromSheet.htm).

Description

This method removes the specified faces from a sheet body.

Syntax (OLE Automation)

void Body.RemoveFacesFromSheet ( numOfFaces,
facesToRemove)

(Table)=========================================================

| Input: | (long) numOfFaces | Number of edges generated when these two bodies are intersected |
| --- | --- | --- |
| Input: | (VARIANT) facesToRemove | VARIANT of type SafeArray of dispatch objects, the faces to remove |

Syntax
(COM)

status = Body->IRemoveFacesFromSheet
( numOfFaces, facesToRemove )

(Table)=========================================================

| Input: | (long) numOfFaces | Number of edges generated when these two bodies are intersected |
| --- | --- | --- |
| Input: | (LPFACE*) facesToRemove | Pointer to an array of the face objects to remove |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

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
<param name="Items" value="Body_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\Body\Body__RemoveFacesFromSheet.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
