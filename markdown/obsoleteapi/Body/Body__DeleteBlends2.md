---
title: "Body::DeleteBlends2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__DeleteBlends2.htm"
---

# Body::DeleteBlends2

This method is obsolete and has been superseded
by[Body2::DeleteBlends2](sldworksAPI.chm::/Body2/Body2__DeleteBlends2.htm).

Description

This method deletes blend faces from an API-generated
body.

Syntax (OLE Automation)

retval = Body2.DeleteBlends2 ( numOfFaces, faceList,
doLocalCheck )

(Table)=========================================================

| Input: | (long) numOfFaces | Number of faces to delete |
| --- | --- | --- |
| Input: | (VARIANT) faceList | List of faces to delete |
| Input: | (BOOL) doLocalCheck | TRUE to perform a local check, FALSE to not |
| Return: | (BOOL) retval | TRUE if successful, FALSE if not |

Syntax (COM)

status = Body2->IDeleteBlends2 ( numOfFaces, faceList,
doLocalCheck, &retval )

(Table)=========================================================

| Input: | (long) numOfFaces | Number of faces to delete |
| --- | --- | --- |
| Input: | (LPFACE) faceList | List of faces to delete of size numOfFaces |
| Input: | (VARIANT_BOOL) doLocalCheck | TRUE to perform a local check, FALSE if not |
| Output: | (VARIANT_BOOL) retval | TRUE if successful, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

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
<param name="Items" value="Body_Object$$**$$ZModifyFace$$**$$ZDeleting$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\Body\Body__DeleteBlends2.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
