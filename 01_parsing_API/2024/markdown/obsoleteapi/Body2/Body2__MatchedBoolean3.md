---
title: "Body2::MatchedBoolean3"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body2/Body2__MatchedBoolean3.htm"
---

# Body2::MatchedBoolean3

This method is obsolete and has been superseded
by[Body2::MatchedBoolean4](sldworksAPI.chm::/Body2/Body2__MatchedBoolean4.htm).

Description

This method performs a matched boolean on the
specified bodies and supports an optional list of faces that match exactly.

Syntax (OLE Automation)

retval = Body2.MatchedBoolean3 ( operationType, toolBody,
numOfMatchingFaces, faceList1, faceList2, errorCode )

(Table)=========================================================

| Input: | (int) operationType | One of the following operation types: SWBODYADD SWBODYCUT SWBODYINTERSECT |
| --- | --- | --- |
| Input: | (VARIANT) toolBody | Array of bodies |
| Input: | (long) numOfMatchingFaces | Number of matching faces |
| Input: | (VARIANT) faceList1 | First face list (see Remarks ) |
| Input: | (VARIANT) faceList2 | Second face list (see Remarks ) |
| Output: | (long) errorCode | Error indicator as defined in swBodyOperationError_e |
| Output: | (VARIANT) retval | Array of bodies formed by the operation |

Syntax (COM)

status = Body2->IMatchedBoolean3 ( operationType,
toolBodyCount, toolBodyArr, numOfMatchingFaces, faceList1, faceList2,
&errorCode, &retval )

Parameters Table Start

(Table)=========================================================

| Input: | (int) operationType | One of these operation types: SWBODYADD SWBODYCUT SWCODYINTERSECT |
| --- | --- | --- |
| Input: | (long) toolBodyCount | Number of bodies |
| Input: | (LPBODY2*) toolBodyArr | Array of bodies of size toolBodyCount |
| Input: | (long) numOfMatchingFaces | Number of matching faces |
| Input: | (LPFACE2*) faceList1 | First face list (see Remarks ) |
| Input: | (LPFACE2*) faceList2 | Second face list (see Remarks ) |
| Output: | (long) errorCode | Error indicated as defined in swBodyOperationError_e |
| Output: | (LPENUMBODIES2) retval | Pointer to the EnumBodies2 object for a list of matches |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The concept of match means that the caller tells the boolean operator
beforehand which faces can be considered to coincide. Basically, the caller
performs part of the boolean operation.

Sometimes the application knows that two faces match because of the
way the bodies are constructed; i.e., the application knows which faces
are intended to match.

Having a list of matching face pairs may allow the matched boolean operator
to resolve other geometric operations that otherwise it would not be able
to work out. In general, providing matched faces speeds up the boolean
operation and makes results more reliable.

The arguments faceList1 and faceList2 arguments can be empty lists.
If matching face pairs are passed in, these faces must match such that:

- the surface geometry is coinciding.
- kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}for
  each edge in a face, there is an edge in the other face that coincides.

This method supports multibody
parts.

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
<param name="Items" value="ZReleaseNotes2003$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\Body2\Body2__MatchedBoolean3.htm" >
<param name="_ID" value="RelatedTopic2" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
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
<param name="Items" value="Body2_Object$$**$$Face2_Object$$**$$EnumBodies2_Object$$**$$Multibody_Parts$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\Body2\Body2__MatchedBoolean3.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
