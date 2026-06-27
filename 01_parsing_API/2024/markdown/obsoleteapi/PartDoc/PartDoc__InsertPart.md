---
title: "PartDoc::InsertPart"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PartDoc/PartDoc__InsertPart.htm"
---

# PartDoc::InsertPart

This
method is obsolete and has been superseded by[PartDoc::InsertPart2.](sldworksAPI.chm::/PartDoc/PartDoc__InsertPart2.htm)

Description

This method inserts an existing part into this
part document.

Syntax (OLE Automation)

retval = PartDoc.InsertPart ( fileName, ImportPlane,
ImportAxis, ImportCThread )

(Table)=========================================================

| Input: | (BSTR) fileName | Name of part file |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) ImportPlane | TRUE if the planes from the part should be imported into this part,
FALSE if not |
| Input: | (VARIANT_BOOL) ImportAxis | TRUE if the axes from the part should be imported into this part, FALSE
if not |
| Input | (VARIANT_BOOL) ImportCThread | TRUE if the cosmetic threads from the part should be imported into this
part, FALSE if not |
| Output: | (LPDISPATCH) retval | Dispatch pointer to the inserted feature |

Syntax (COM)

status = PartDoc->InsertPart ( fileName, ImportPlane,
ImportAxis, ImportCThread, &retval )

Parameters Table Start

(Table)=========================================================

| Input: | (BSTR) fileName | Name of part file |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) ImportPlane | TRUE if the planes from the part should be imported into this part,
FALSE if not |
| Input: | (VARIANT_BOOL) ImportAxis | TRUE if the axes from the part should be imported into this part, FALSE
if not |
| Input: | (VARIANT_BOOL) ImportCThread | TRUE if the cosmetic threads from the part should be imported into this
part, FALSE if not |
| Output: | (LPFEATURE) retval | Pointer to the inserted feature |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method inserts the specified
part at the origin of this part. To position the insert part at a different
location or orientation or both, use FeatureManager::InsertMoveCopyBody2.

The interface returned by
this method is LPFEATURE, which gives you access to the Feature APIs,
such as Feature::Name to get or set the name of the feature.

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
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\PartDoc\PartDoc__InsertPart.htm" >
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
<param name="Items" value="PartDoc_Object$$**$$Feature_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\PartDoc\PartDoc__InsertPart.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
