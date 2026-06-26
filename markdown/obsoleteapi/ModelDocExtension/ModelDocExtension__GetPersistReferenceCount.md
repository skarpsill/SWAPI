---
title: "ModelDocExtension::GetPersistReferenceCount"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDocExtension/ModelDocExtension__GetPersistReferenceCount.htm"
---

# ModelDocExtension::GetPersistReferenceCount

This method is obsolete and has been superseded
by[ModelDocExtension::GetPersistReferenceCount3](sldworksAPI.chm::/ModelDocExtension/ModelDocExtension__GetPersistReferenceCount3.htm).

Description

This method gets the size
of the persistent reference ID assigned to the selected object in this
model document.

Syntax (OLE Automation)

*count = ModelDocExtension.GetPersistReferenceCount
( dispObj)

(Table)=========================================================

| Input: | (LPDISPATCH) dispObj | Dispatch pointer to the selected
object |
| --- | --- | --- |
| Output: | (long *) *count | Size of that object's persistent
reference ID |

Syntax (COM)

status = ModelDocExtension->GetPersistReferenceCount
( dispObj, &*count)

Parameters Table Start

(Table)=========================================================

| Input: | (LPDISPATCH) dispObj | Dispatch pointer to the selected object |
| --- | --- | --- |
| Output: | (long *) *count | Size of that object's persistent reference ID |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Call this method before calling the COM version
ModelDocExtension::GetPersistReference.

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
<param name="Items" value="ZReleaseNotes004$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\ModelDocExtension\ModelDocExtension__GetPersistReferenceCount.htm" >
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
<param name="Items" value="ModelDocExtension_Object$$**$$ModelDocExtensionPersistentObject$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\ModelDocExtension\ModelDocExtension__GetPersistReferenceCount.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
