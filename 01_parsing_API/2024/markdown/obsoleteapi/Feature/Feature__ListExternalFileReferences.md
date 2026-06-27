---
title: "Feature::ListExternalFileReferences"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Feature/Feature__ListExternalFileReferences.htm"
---

# Feature::ListExternalFileReferences

This method is obsolete and has been superseded
by[Feature::ListExternalFileReferences2](sldworksAPI.chm::/Feature/Feature__ListExternalFileReferences2.htm).

Description

This method gets the names and status of the
external file references on this model.

Syntax (OLE Automation)

void = Feature.ListExternalFileReferences ( modelPathName,
componentPathName, feature, dataType, Status, refEntity, featCom )

(Table)=========================================================

| Output: | (VARIANT) *modelPathName | Array of external model references |
| --- | --- | --- |
| Output: | (VARIANT) *componentPathName | Array of external component references |
| Output: | (VARIANT) *feature | Array of external feature references |
| Output: | (VARIANT) *dataType | Array of types of data |
| Output: | (VARIANT) *Status | Status of external reference as defined in swExternalReferenceStatus_e |
| Output: | (VARIANT) *refEntity | Array of external entity references |
| Output: | (VARIANT) *featCom | Array of feature components |

Syntax (COM)

status = Feature->IListExternalFileReferences
( numRefs, modelPathName, compPathName, feature, dataType, Status, refEntity,
featComp )

Parameters Table Start

(Table)=========================================================

| Input: | (long) numRefs | Number of external references |
| --- | --- | --- |
| Output: | (BSTR*) modelPathName | Array of external model references of size
numRefs |
| Output: | (BSTR*) compPathName | Array of external component references of
size numRefs |
| Output: | (BSTR*) feature | Array of external feature references of size
numRefs |
| Output: | (BSTR*) dataType | Array of types of data of size numRefs |
| Output: | (long*) Status | Status of external reference as defined in swExternalReferenceStatus_e |
| Output: | (BSTR*) refEntity | Array of external entity references of size
numRefs |
| Output: | (BSTR*) featComp | Array of feature components of size numRefs |
| Return: | (HRESULT) status | S_OK if successful |

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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\Feature\Feature__ListExternalFileReferences.htm" >
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
<param name="Items" value="Feature Method$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\Feature\Feature__ListExternalFileReferences.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic3
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
<param name="Items" value="RetrieveExtRef_Example$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\Feature\Feature__ListExternalFileReferences.htm" >
<param name="_ID" value="RelatedTopic3" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
