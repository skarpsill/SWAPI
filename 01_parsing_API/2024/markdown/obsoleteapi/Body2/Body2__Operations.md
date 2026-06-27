---
title: "Body2::Operations"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body2/Body2__Operations.htm"
---

# Body2::Operations

This method is obsolete and has been superseded by[Body2::Operations2](sldworksAPI.chm::/Body2/Body2__Operations2.htm).

Description

This method performs add, cut, and intersect (unite, subtract, and interfere)
operations between two temporary bodies.

Syntax (OLE Automation)

retval = Body2.Operations ( operationType,
toolBody, NumMaxSections )

(Table)=========================================================

| Input: | (int) operationType | One of the operation types: SWBODYADD SWBODYCUT SWBODYINTERSECT |
| --- | --- | --- |
| Input: | (LPDISPATCH) toolBody | Dispatch pointer for the tool body |
| Input: | (long) NumMaxSections | Maximum number of bodies that can be returned (set by the application) |
| Return: | (VARIANT) retval | SafeArray containing a set of LPDISPATCH pointers for the resulting
bodies |

Syntax (COM)

status = Body2->IOperations ( operationType,
toolBody, NumMaxSections, resultingBodies, &retval )

(Table)=========================================================

| Input: | (int) operationType | One of the operation types: SWBODYADD SWBODYCUT SWBODYINTERSECT |
| --- | --- | --- |
| Input: | (LPBODY2) toolBody | Pointer to the tool body |
| Input: | (long) NumMaxSections | Maximum number of bodies that can be returned (set by the application) |
| Input: | (LPBODY2*) resultingBodies | Array of pointers to the resulting bodies |
| Output: | (long) retval | Number of bodies returned |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method works with two temporary bodies: the target and the tool.
The output is the list of bodies resulting from the operation.

Pointers to the two temporary bodies (Body and toolBody) are invalid
when the operation is complete. COM applications should release these
two pointers after calling this method. If your application needs to maintain
these bodies, then use Body2::Copy to make copies before you pass them
to this method.

Use the NumMaxSections argument with COM applications to limit the number
of bodies returned so that the array does not overflow. For Dispatch applications,
set NumMaxSections to -1 and SolidWorks returns all the resulting bodies.

To perform a SWBODYINTERSECT between a sheet body and a solid body,
the sheet body must be the target body.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic2
dtcid=2
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
<param name="Items" value="ZReleaseNotes2001Plus$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\body2\Body2__Operations.htm" >
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
dtcid=3
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
<param name="Items" value="Body2_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\body2\Body2__Operations.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
