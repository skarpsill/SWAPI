---
title: "SWDesignCheck::RunDesignCheck"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SWDesignCheck/SWDesignCheck__RunDesignCheck.htm"
---

# SWDesignCheck::RunDesignCheck

This method is obsolete and has been superseded
by[SWDesignCheck::RunDesignCheck2](sldworksAPI.chm::/SWDesignCheck/SWDesignCheck__RunDesignCheck2.htm).

Description

This method runs the SolidWorks Design Checker
using the specified requirements document. This method can also add a
new, or overwrite, an existing the report to the Design Binder.

Syntax (OLE Automation)

retval = SWDesignCheck->RunDesignCheck ( StandardFileName,
ReportFolderName, AddtoDesignBinder, bOverWriteReport)

Parameters Table Start

(Table)=========================================================

| Input: | (BSTR) StandardFileName | Path and filename of SolidWorks Design Checker requirements document |
| --- | --- | --- |
| Input: | (BSTR) ReportFolderName | Name of report NOTE: A filename extension of .dxp is automatically appended
the specified filename. The report is an XML file. |
| Input: | (VARIANT_BOOLEAN) AddtoDesignBinder | TRUE to add the report to the Design Binder, FALSE to not |
| Input: | (VARIANT_BOOLEAN) bOverWriteReport | TRUE to overwrite any existing report of the same name in the Design
Binder, FALSE to not |
| Return: | (long) retval | Error code as defined in dsgnchkError_e |

Syntax (COM)

status = SWDesignCheck->RunDesignCheck ( StandardFileName,
ReportFolderName, AddtoDesignBinder, bOverWriteReport, &retval)

Parameters Table Start

Parameters Table Start

(Table)=========================================================

| Input: | (BSTR) StandardFileName | Path and filename of SolidWorks Design Checker requirements document |
| --- | --- | --- |
| Input: | (BSTR) ReportFolderName | Name of report NOTE: A filename extension of .dxp is automatically appended
the specified filename. The output report is an XML file. |
| Input: | (VARIANT_BOOLEAN) AddtoDesignBinder | TRUE to add the report to the Design Binder, FALSE to not |
| Input: | (VARIANT_BOOLEAN) bOverWriteReport | TRUE to overwrite any existing report of the same name in the Design
Binder, FALSE to not |
| Output: | (long) retval | Error code as defined in dsgnchkError_e |
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
<param name="Items" value="ZReleaseNotes2006$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\SWDesignCheck\SWDesignCheck__RunDesignCheck.htm" >
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
<param name="Items" value="SWDesignCheck_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\SWDesignCheck\SWDesignCheck__RunDesignCheck.htm" >
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
<param name="Items" value="EXRunSolidWorksDesignChecker$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\SWDesignCheck\SWDesignCheck__RunDesignCheck.htm" >
<param name="_ID" value="RelatedTopic5" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
