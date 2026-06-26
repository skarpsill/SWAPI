---
title: "ModelDocExtension::GetObjectByPersistReference2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDocExtension/ModelDocExtension__GetObjectByPersistReference2.htm"
---

# ModelDocExtension::GetObjectByPersistReference2

This method is obsolete and has been superseded
by[ModelDocExtension::GetObjectByPersistReference3.](sldworksAPI.chm::/ModelDocExtension/ModelDocExtension__GetObjectByPersistReference3.htm)

Description

This method gets the object
assigned to the specified persistent reference ID.

NOTE:A persistent reference ID is related to a model. It is portable and can
be saved within the model or in other places. Some persistent reference
IDs are general to all models and can be instantiated from all models.
Your application must handle persistent reference IDs and their relationships
among models.

Syntax (OLE Automation)

*dispObj = ModelDocExtension.GetObjectByPersistReference2
( persistId, *errorCode)

(Table)=========================================================

| Input: | (VARIANT) persistId | Object's persistent reference
ID (see Remarks ) |
| --- | --- | --- |
| Output: | (long ) *errorCode | Success or error code as defined by swPersistReferencedObjectStates_e
(see Remarks ) |
| Output: | (LPDISPATCH ) *dispObj | Dispatch pointer to the object |

Parameters Table End

Syntax (COM)

status = ModelDocExtension->IGetObjectByPersistReference2
( count, *persistId, *errorCode, &dispObj)

Parameters Table Start

(Table)=========================================================

| Input: | (long) count | Size of persistent reference
ID (see Remarks ) |
| --- | --- | --- |
| Input: | (BYTE ) *persistId | Persistent reference ID (see Remarks ) |
| Output: | (long ) *errorCode | Success or error code as defined by swPersistReferencedObjectStates_e
(see Remarks ) |
| Output: | (LPDISPATCH ) *dispObj | Dispatch pointer to the object |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Before calling this method:

1. If
  using the COM version of this method, call ModelDocExtension::GetPersistentReferenceCount
  to determine the size of the persistent reference ID.
2. Call
  ModelDocExtension::GetPersistReference to get the object's persistent
  reference ID.

The swPersistReferencedObject_Suppressed
andswPersistReferencedObject_Deleted
enumerators only apply to references of topological entities.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic2
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ZReleaseNotes004plus$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\ModelDocExtension\ModelDocExtension__GetObjectByPersistReference2.htm" >
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
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\ModelDocExtension\ModelDocExtension__GetObjectByPersistReference2.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic5
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
<param name="Items" value="EXPersistentReferenceID$$**$$EXUsePersistentReferences$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\ModelDocExtension\ModelDocExtension__GetObjectByPersistReference2.htm" >
<param name="_ID" value="RelatedTopic5" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
