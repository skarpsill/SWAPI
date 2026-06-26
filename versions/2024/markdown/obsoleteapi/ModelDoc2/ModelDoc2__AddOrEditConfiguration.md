---
title: "ModelDoc2::AddOrEditConfiguration"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__AddOrEditConfiguration.htm"
---

# ModelDoc2::AddOrEditConfiguration

This
method is obsolete and has been superseded by Configuration::GetParameters and Configuration::SetParameters .

Description

This method adds or edits
a configuration in the model document.

Syntax (OLE Automation)

retval = ModelDoc2.AddOrEditConfiguration ( ConfigName,
paramNames, paramValues )

(Table)=========================================================

| Input: | (BSTR) ConfigName | Name of the configuration |
| --- | --- | --- |
| Input: | (VARIANT) paramNames | Array of parameters (see Remarks ) |
| Input: | (VARIANT) paramValues | Array of values (see Remarks ) |
| Output: | (long) retval | Indicates success or failure |

Syntax (COM)

status = ModelDoc2->IAddOrEditConfiguration (
ConfigName, paramCount, paramNames, paramValues, &retval )

Parameters Table Start

(Table)=========================================================

| Input: | (BSTR) ConfigName | Name of the configuration |
| --- | --- | --- |
| Input: | (long) paramCount | Number of parameters |
| Input: | (BSTR*) paramNames | Array of parameters of size paramCount (see Remarks ) |
| Input: | (BSTR) *paramValues | Array of values of size paramCount (see Remarks ) |
| Output: | (long) retval | Indicates success or failure |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

You can control the following items in a part
document:

- Dimension values. Specify
  the dimension name in paramNames (for example, D1@Sketch1) and the value
  in paramValues (for example, 60.0mm).
- Suppression state of
  features. Specify the feature name in paramNames (for example, $STATE@Extrude2)
  and the suppression state in paramValues (S=suppressed or U=Unsuppressed)
  .

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
<param name="Items" value="ZReleaseNotes2003$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\ModelDoc2\ModelDoc2__AddOrEditConfiguration.htm" >
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
<param name="Items" value="ModelDoc2_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\ModelDoc2\ModelDoc2__AddOrEditConfiguration.htm" >
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
<param name="Items" value="EXAddEditConfigurations$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\ModelDoc2\ModelDoc2__AddOrEditConfiguration.htm" >
<param name="_ID" value="RelatedTopic4" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
