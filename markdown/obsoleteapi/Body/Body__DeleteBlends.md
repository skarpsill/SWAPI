---
title: "Body::DeleteBlends"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__DeleteBlends.htm"
---

# Body::DeleteBlends

This
method is obsolete and has been superceded by[Body::DeleteBlends2](Body__DeleteBlends2.htm)

Description

This method removes a set of fillet faces from
a temporary body and heals the body.

Syntax (OLE Automation)

retval = Body.DeleteBlends (VARIANT
faceList)

(Table)=========================================================

| Input: | (VARIANT) faceList | SafeArray of blend faces to delete |
| --- | --- | --- |
| Return: | (BOOL) retval | TRUE if successful, FALSE if error |

Syntax (COM)

status = Body->DeleteBlends ( long numOfFaces,
LPFACE* faceList, VARIANT_BOOL &retval )

(Table)=========================================================

| Input: | (long) numOfFaces | Number of faces in array |
| --- | --- | --- |
| Input: | (LPFACE*) faceList | List of Face objects to delete |
| Output: | (VARIANT_BOOL) retval | TRUE if successful, FALSE if error |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The body is modified.

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
<param name="Items" value="ZReleaseNotes2000$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\Body\Body__DeleteBlends.htm" >
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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\Body\Body__DeleteBlends.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
