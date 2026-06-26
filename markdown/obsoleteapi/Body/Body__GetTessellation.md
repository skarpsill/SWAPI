---
title: "Body::GetTessellation"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__GetTessellation.htm"
---

# Body::GetTessellation

This
method is obsolete and has been superseded by[Body2::GetTessellation](sldworksAPI.chm::/Body2/Body2__GetTessellation.htm).

Description

This method gets the Tessellation object.

Syntax (OLE Automation)

retval = Body.GetTessellation ( FaceList )

(Table)=========================================================

| Input: | (VARIANT) FaceList | VARIANT of type SafeArray of pointers to dispatch
objects, the array of faces to tessellate; if this is empty, then SolidWorks
tessellates the body |
| --- | --- | --- |
| Return: | (LPDISPATCH) retval | Pointer to the dispatch object for the Tessellation
object |

Syntax (COM)

status = Body->IGetTessellation ( numOfFaces,
FaceList, &retval )

(Table)=========================================================

| Input: | (long) numOfFaces | Number of faces |
| --- | --- | --- |
| Input: | (LPFACE*) FaceList | Array of faces to tessellate of size numOfFaces;
if this is NULL, then tessellate the body |
| Output: | (LPTESSELLATION) retval | Pointer to the Tessellation object |
| Return: | (HRESULT) status | S_OK if successful. |

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
<param name="Items" value="ZReleaseNotes2001$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\Body\Body__GetTessellation.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Body_Object$$**$$ZTessellation$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\Body\Body__GetTessellation.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
