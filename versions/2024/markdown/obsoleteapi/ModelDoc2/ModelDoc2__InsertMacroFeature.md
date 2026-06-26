---
title: "ModelDoc2::InsertMacroFeature"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__InsertMacroFeature.htm"
---

# ModelDoc2::InsertMacroFeature

This method is obsolete and has been superseded
by[FeatureManager::InsertMacroFeature](../FeatureManager/FeatureManager__InsertMacroFeature.htm).

Description

This method inserts a macro feature into the
model.

Syntax (OLE Automation)

retval = ModelDoc2.InsertMacroFeature ( cmdFile,
cmdModule, cmdProcedure, paramNames, paramTypes, paramValues, pmFile,
pmModule, pmProcedure )

(Table)=========================================================

| Input: | (BSTR) cmdFile | Macro file executed during feature regeneration |
| --- | --- | --- |
| Input: | (BSTR) cmdModule | Source module executed during feature regeneration |
| Input: | (BSTR) cmdProcedure | Source procedure executed during feature regeneration |
| Input: | (Variant) paramNames | Array of parameter names |
| Input: | (Variant) paramTypes | Array of parameter types as defined in swMacroFeatureParamType_e |
| Input: | (Variant) paramValues | Array of parameter values |
| Input: | (BSTR) pmFile | Macro file executed after edit definition is selected |
| Input: | (BSTR) pmModule | Source module executed after edit definition is selected |
| Input: | (BSTR) pmProcedure | Source procedure executed after edit definition is selected |
| Output: | (LPDISPATCH) retval | Pointer to macro feature |

Syntax (COM)

status = ModelDoc2->IInsertMacroFeature ( cmdFile,
cmdModule, cmdProcedure, paramCount, paramNames, paramTypes, paramValues,
pmFile, pmModule, pmProcedure, &retval )

Parameters Table Start

(Table)=========================================================

| Input: | (BSTR) cmdFile | Macro file executed during feature regeneration |
| --- | --- | --- |
| Input: | (BSTR) cmdModule | Source module executed during feature regeneration |
| Input: | (BSTR) cmdProcedure | Source procedure executed during feature regeneration |
| Input: | (long) paramCount | Number of parameters |
| Input: | (BSTR) *paramNames | Array of size paramCount |
| Input: | (long) *paramTypes | Array of parameter types as defined in swMacroFeatureParamType_e
of size paramCount |
| Input: | (BSTR) *paramValues | Array of size paramCount |
| Input: | (BSTR) pmFile | Macro file executed after edit definition is selected |
| Input: | (BSTR) pmModule | Source module executed after edit definition is selected |
| Input: | (BSTR) pmProcedure | Source procedure executed after edit definition is selected |
| Output: | (LPFEATURE) retval | Pointer to macro feature |
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
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\ModelDoc2\ModelDoc2__InsertMacroFeature.htm" >
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
<param name="Items" value="ModelDoc2 Method$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\ModelDoc2\ModelDoc2__InsertMacroFeature.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
