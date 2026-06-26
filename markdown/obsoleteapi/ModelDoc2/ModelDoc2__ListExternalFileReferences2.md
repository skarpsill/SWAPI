---
title: "ModelDoc2::ListExternalFileReferences2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__ListExternalFileReferences2.htm"
---

# ModelDoc2::ListExternalFileReferences2

This method is obsolete and has been superseded
by[ModelDocExtension::ListExternalFileReferences](sldworksAPI.chm::/ModelDocExtension/ModelDocExtension__ListExternalFileReferences.htm).

Description

This method gets the names and statuses of
the external file references on this model.

Syntax (OLE Automation)

void = ModelDoc2.ListExternalFileReferences2 ( modelPathName,
componentPathName, feature, dataType, Status, refEntity, featCom )

(Table)=========================================================

| Output: | (VARIANT) *modelPathName | Array of external parts' or assemblies' paths and names |
| --- | --- | --- |
| Output: | (VARIANT) *componentPathName | Array of configurations of the referenced components to use for derived
parts |
| Output: | (VARIANT) *feature | Array of in-context items (sketches, features, and so on) in the selected
part |
| Output: | (VARIANT) *dataType | Array of data used to create the items (converted edge or face, converted
or offset sketch entity, body, and so on) |
| Output: | (VARIANT) *Status | Status of external reference as defined in swExternalReferenceStatus_e |
| Output: | (VARIANT) *refEntity | Array of actual items being used and the names of the documents that
contain the items |
| Output: | (VARIANT) *featCom | Array of the names of the components in which the affected features
exist; this information is only displayed when one or more refEntity is
in a different component in an assembly; this does not apply to derived
parts |

Syntax (COM)

status = ModelDoc2->IListExternalFileReferences2
( numRefs, modelPathName, compPathName, feature, dataType, Status, refEntity,
featComp )

Parameters Table Start

(Table)=========================================================

| Input: | (long) numRefs | Number of external references |
| --- | --- | --- |
| Output: | (BSTR*) modelPathName | Array of external parts' or assemblies' paths
and names of size numRefs |
| Output: | (BSTR*) compPathName | Array of configurations of the referenced
components to use for derived parts of size numRefs |
| Output: | (BSTR*) feature | Array of in-context items (sketches, features,
and so on) in the selected part of size numRefs |
| Output: | (BSTR*) dataType | Array of data used to create the items (converted
edge or face, converted or offset sketch entity, body, and so on) of size
numRefs |
| Output: | (long*) Status | Status of external reference as defined in swExternalReferenceStatus_e |
| Output: | (BSTR*) refEntity | Array of actual items being used and the
names of the documents that contain the items of size numRefs |
| Output: | (BSTR*) featComp | Array of the names of the components in which
the affected features exist of size numRefs; this information is only
displayed when one or more refEntity is in a different component in an
assembly; this does not apply to derived parts |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Call ModelDoc2::ListExternalFileReferencesCount2
before calling the COM version of this method to determine the size of
the array required.

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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\ModelDoc2\ModelDoc2__ListExternalFileReferences2.htm" >
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
<param name="Items" value="ModelDoc2_Object$$**$$ExternalReferences$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\ModelDoc2\ModelDoc2__ListExternalFileReferences2.htm" >
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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\ModelDoc2\ModelDoc2__ListExternalFileReferences2.htm" >
<param name="_ID" value="RelatedTopic3" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
