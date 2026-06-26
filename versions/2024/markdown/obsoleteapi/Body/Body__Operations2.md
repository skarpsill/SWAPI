---
title: "Body::Operations2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__Operations2.htm"
---

# Body::Operations2

This method is obsolete and has been superseded
byBody2::Operations2 .

Description

This method performs add, cut, and intersect (unite, subtract, interfere)
operations between two temporary bodies.

Syntax (OLE Automation)

retval = Body2.Operations2 ( operationType, toolBody,
&errorCode )

(Table)=========================================================

| Input: | (int) operationType | One of the following operation types: SWBODYADD SWBODYCUT SWBODYINTERSECT |
| --- | --- | --- |
| Input: | (LPDISPATCH) toolBody | Dispatch pointer to the tool body |
| Output: | (long) errorCode | Error indicator as defined in swBodyOperationError_e ; returns
swBodyOperationNoError if SolidWorks does not generate an error |
| Return: | (VARIANT) retval | Array of pointers to the resulting bodies |

Syntax (COM)

status = Body2->IOperations2 ( operationType,
toolBody, &errorCode, &resultingBodies )

(Table)=========================================================

| Input: | (int) operationType | Operation types (see Remarks ) |
| --- | --- | --- |
| Input: | (LPBODY2) toolBody | Pointer to the tool body |
| Output: | (long) errorCode | Error indicator as defined in swBodyOperationError_e ; returns
swBodyOperationNoError if SolidWorks does not generate an error |
| Output: | (LPENUMBODIES2) resultingBodies | Enumerated list of the resulting bodies |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

If the target and tool bodies are the same in geometry,
the result body of this method is NULL and the return value is be S_FALSE.

This method works with two temporary bodies, one
is used as the target and one is used as the tool. The output is a list
of bodies resulting from the operation.

The two temporary bodies used in this function
(the Body and toolBody pointers) will be invalid once the operation is
complete. COM applications should Release these two pointers after calling
this function. If your application needs to maintain these bodies, then
you should make a copy of them using Body2::Copy before passing them to
this routine.

To perform a SWBODYINTERSECT between a sheet body
and a solid body, the sheet body must be the target body.

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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\Body\Body__Operations2.htm" >
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
<param name="Items" value="Body_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\Body\Body__Operations2.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
