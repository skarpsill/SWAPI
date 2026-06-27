---
title: "ModelDocExtension::GetPersistReference"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDocExtension/ModelDocExtension__GetPersistReference.htm"
---

# ModelDocExtension::GetPersistReference

This method is obsolete and has been superseded
by[ModelDocExtension::GetPersistReference3](sldworksAPI.chm::/ModelDocExtension/ModelDocExtension__GetPersistReference3.htm).

Description

This method gets the persistent
reference ID for the specified object in this model document.

Syntax (OLE Automation)

persistId = ModelDocExtension.GetPersistReference
( dispObj)

(Table)=========================================================

| Input: | (LPDISPATCH) dispObj | Dispatch pointer to the object |
| --- | --- | --- |
| Output: | (VARIANT*) persistId | VARIANT of type SafeArray containing
the persistent reference ID assigned to that object |

Syntax (COM)

status = ModelDocExtension->IGetPersistReference
( dispObj, count, &persistId)

Parameters Table Start

(Table)=========================================================

| Input: | (LPDISPATCH) dispObj | Dispatch pointer to the object |
| --- | --- | --- |
| Input: | (long) count | Size of persistId assigned to
that object (see Remarks ) |
| Output: | (BYTE*) persistId | Byte array containing the persistent reference
ID assigned to that object |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

To get the size of the byte array, call ModelDocExtension::GetPersistReferenceCount
before calling this method.

The internal representations of the persistId array
may change, possibly from rebuild to rebuild, or more likely, from one
release of SolidWorks to the next, but their usage in finding the correct
entity will be consistent across rebuilds and SolidWorks releases.

To compare the referenced entities, you could use
the Visual BasicIsoperator to
find out if the entities are the same.

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
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\ModelDocExtension\ModelDocExtension__GetPersistReference.htm" >
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
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\ModelDocExtension\ModelDocExtension__GetPersistReference.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic4
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
<param name="Items" value="EXPersistentReferenceID$$**$$EXUsePersistentReferences$$**$$EXCheckFacesFaults$$**$$EXCheckEdgesFaults$$**$$EXGetPersistentReferenceID$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\ModelDocExtension\ModelDocExtension__GetPersistReference.htm" >
<param name="_ID" value="RelatedTopic4" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
