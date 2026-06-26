---
title: "Body2::DraftBody"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body2/Body2__DraftBody.htm"
---

# Body2::DraftBody

This body is obsolete and has been superseded
by[Body2::DraftBody2](sldworksAPI.chm::/Body2/Body2__DraftBody2.htm).

Description

This method adds a draft angle to a set of
faces on a temporary body. This method modifies the body.

Syntax (OLE Automation)

retval = Body2.DraftBody (numOfEnts,
faceList, edgeList, draftAngle, dir)

(Table)=========================================================

| Input: | (long) numOfEnts | Number of faces to draft |
| --- | --- | --- |
| Input: | (VARIANT) faceList | List of pointers to the faces |
| Input: | (VARIANT) edgeList | List of pointers to the reference edges, one
for each face, along which the draft is applied |
| Input: | (double) draftAngle | Draft angle |
| Input: | (VARIANT) dir | VARIANT of type SafeArray of 3 doubles (x,y,z),
a vector which specifies the direction of the draft |
| Return: | (BOOL) retval | TRUE if draft successfully applied, FALSE if
not |

Syntax (COM)

status = Body2->IDraftBody ( numOfEnts, faceList,
edgeList, draftAngle, dir, &retval )

(Table)=========================================================

| Input: | (long) numOfEnts | Number of faces to draft |
| --- | --- | --- |
| Input: | (LPFACE*) faceList | List of pointers to the faces |
| Input: | (LPEDGE*) edgeList | List of pointers to the reference edges, one
for each face, along which the draft is applied |
| Input: | (double) draftAngle | Draft angle |
| Input: | (double*) dir | Pointer to an array of 3 doubles (x,y,z), a vector
which specifies the direction of the draft |
| Output: | (VARIANT_BOOL) retval | TRUE if draft successfully applied, FALSE if
not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

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
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\obsoleteapi\Body2\Body2__DraftBody.htm" >
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
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\obsoleteapi\Body2\Body2__DraftBody.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
