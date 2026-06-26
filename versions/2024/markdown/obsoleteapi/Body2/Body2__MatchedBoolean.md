---
title: "Body2::MatchedBoolean"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body2/Body2__MatchedBoolean.htm"
---

# Body2::MatchedBoolean

This
method is obsolete and has been superseded by[Body2::MatchedBoolean3](Body2__MatchedBoolean3.htm).

Description

This method performs a matched boolean on the
specified faces.

Syntax (OLE Automation)

retval = Body2.MatchedBoolean ( operationType, toolBody,
numOfMatchingFaces, faceList1, faceList2, errorCode )

(Table)=========================================================

| Input: | (int) operationType | One of the following operation types: SWBODYADD SWBODYCUT SWBODYINTERSECT |
| --- | --- | --- |
| Input: | (LPDISPATCH) toolBody | Pointer to the tool body |
| Input: | (long) numOfMatchingFaces | Number of matching faces |
| Input: | (VARIANT) faceList1 | First face list |
| Input: | (VARIANT) faceList2 | Second face list |
| Output: | (long) errorCode | Error indicator as defined in swBodyOperationError_e |
| Output: | (VARIANT) retval | SafeArray containing a set of LPDISPATCH pointers for the resulting
matches |

Syntax (COM)

status = Body2->IMatchedBoolean ( operationType,
toolBody, numOfMatchingFaces, faceList1, faceList2, &errorCode, &retval
)

Parameters Table Start

(Table)=========================================================

| Input: | (int) operationType | One of the following operation types: SWBODYADD SWBODYCUT SWBODYINTERSECT |
| --- | --- | --- |
| Input: | (LPBODY) toolBody | Pointer to the tool body |
| Input: | (long) numOfMatchingFaces | Number of matching faces |
| Input: | (LPFACE*) faceList1 | First face list |
| Input: | (LPFACE*) faceList2 | Second face list |
| Output: | (long) errorCode | Error indicator as defined in swBodyOperationError_e |
| Output: | (LPENUMBODIES) retval | Pointer to an EnumBodies2 object for the resulting matches |
| Return: | (HRESULT) status | S_OK if successful |

Parameters Table End

Remarks

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
<param name="Items" value="ZReleaseNotes2001Plus$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\Body2\Body2__MatchedBoolean.htm" >
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
<param name="Items" value="Body2_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\Body2\Body2__MatchedBoolean.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
