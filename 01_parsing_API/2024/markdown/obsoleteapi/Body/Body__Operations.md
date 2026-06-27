---
title: "Body::Operations"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__Operations.htm"
---

# Body::Operations

This method is obsolete and has been superseded
by[Body::Operations2](Body__Operations2.htm).

Description

This method adds, cuts, and intersects two temporary bodies.

Syntax (OLE Automation)

retval = Body.Operations ( operationType,
toolBody, NumMaxSections )

(Table)=========================================================

| Input: | (int) operationType | One of the following operation types: SWBODYADD SWBODYCUT SWBODYINTERSECT |
| --- | --- | --- |
| Input: | (LPDISPATCH) toolBody | Dispatch pointer for the tool body |
| Input: | (long) NumMaxSections | Maximum number of bodies that can be returned (set by the application) |
| Return: | (VARIANT) retval | SafeArry containing a set of pointers for the resulting bodies |

Syntax
(COM)

status = Body->IOperations ( operationType,
toolBody, NumMaxSections, resultingBodies, &retval )

(Table)=========================================================

| Input: | (int) operationType | One of the following operation types: SWBODYADD SWBODYCUT SWBODYINTERSECT |
| --- | --- | --- |
| Input: | (LPBODY) toolBody | Pointer to the tool body |
| Input: | (long) NumMaxSections | Maximum number of bodies that can be returned (set by the application) |
| Input: | (LPBODY*) resultingBodies | Array of pointers to the resulting bodies |
| Output: | (long) retval | Number of bodies returned |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method works with two temporary bodies, one is the target and the
other is the tool. The output is a list of bodies resulting from the operation.

The two temporary bodies used by this method (the Body and toolBody
pointers) are invalid wehn the operation is complete. COM applications
should release these two pointers after using this method. If your application
needs to maintain these bodies, then make a copy using Body::Copy
before passing them to this routine.

COM applications should use the MaxNumberOfSections argument to limit
the number of bodies returned so that the array does not overflow. For
Dispatch applications, set MaxNumberOfSections to -1 and SolidWorks returns
all the resulting bodies.

To perform a SWBODYINTERSECT between a sheet body and a solid body,
the sheet body must be the target body.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name=_Version value="65536" >
<param name=_ExtentX value="1323" >
<param name=_ExtentY value="556" >
<param name=_StockProps value="13" >
<param name=ForeColor value="0" >
<param name=BackColor value="12632256" >
<param name=UseButton value="0" >
<param name=ControlLabel value="See Also" >
<param name=UseIcon value="0" >
<param name=Items value="Body_Object$$**$$ZCreateBody$$**$$" >
<param name=Image value="" >
<param name=FontInfo value="MS Sans Serif,8,0,," >
<param name=_CURRENTFILEPATH value="C:\Home\Oneill\Body\Body__Operations.htm" >
<param name=_ID value="RelatedTopic0" >
<param name=DialogDisplay value="0" >
<param name=Frame value="" >
<param name=Window value="" >
<param name=ChmFile value="" >
<param name=DisableJump value="0" >
</object>Metadata type="DesignerControl" endspan
