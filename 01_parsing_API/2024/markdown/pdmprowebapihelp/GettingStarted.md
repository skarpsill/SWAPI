---
title: "Getting Started"
project: "PDM Pro Web API Help"
interface: ""
member: ""
kind: "topic"
source: "pdmprowebapihelp/GettingStarted.html"
---

# Getting Started

- [Prerequisites](#Prerequisites)
- [Research and Development](#research)
- [Javascript, Python, and C# Console Examples](#examples)
- [Install and Enable CORS](#CORS)

##### Prerequisites

In order to build applications that use the operations in the SOLIDWORKS PDM Professional Web API, you need:

- SOLIDWORKS PDM Professional

Read the**Installation Guide.pdf**in**c:\Program Files\SOLIDWORKS Corp\SOLIDWORKS PDM\Lang\ lang**. Follow the outline in**Chapter 2 Installation Overview**and all the instructions in ensuing chapters to install required and optional (SOLIDWORKS PDM Professional only) components.

- SOLIDWORKS PDM Web API Server (SOLIDWORKS PDM Professional only)

In the installation guide, follow the instructions under**Chapter 5 Installing SOLIDWORKS PDM - Installing SOLIDWORKS PDM Web API Server.**At**https://help.solidworks.com**select a version and a language and navigate to**SOLIDWORKS PDM >****SOLIDWORKS PDM Administration Tool > Administering Web API Servers (For SOLIDWORKS PDM Professional only)**). Using the PDM Administration Tool, you must add the web API server, add a vault to the web API server, and configure the vault.

- Cross-origin resource sharing (CORS)

If you are not familiar with CORS, then please google**Cross-origin resource sharing.**CORS is required if you use browser-based programming languages like Java, PHP, Javascript, Python, NodeJs etc. or access the PDM Pro Web API from a different domain. If Internet Information Services (IIS) is not already active, google "how to open internet information services", and follow the instructions. Then[install CORS](#CORS)and configure the SWPDMWebAPI web site in IIS to enable CORS. See the Javascript and Python examples in[api/{vaultName}/authenticate](PDM%20Pro%20API_ws~r-api-{vaultName}-authenticate~o-HttpPost.html).

- Microsoft Visual Studio (for C# and ASP.NET)

You can use a .NET project template to create a C# Console App (.NET Core) or an ASP.NET Web Application (.NET Framework) that accesses the PDM Pro Web API. See the C# console application example in[api/{vaultName}/authenticate](PDM%20Pro%20API_ws~r-api-{vaultName}-authenticate~o-HttpPost.html).

##### Research and Development

The SOLIDWORKS PDM Professional Web API is an extension of Microsoft's[ASP.NET Web API](https://docs.microsoft.com/en-us/aspnet/web-api/)which is a framework that allows you to create Representational State Transfer (REST) applications on the .NET Framework.

If you are not familiar with REST, then please google:

- Representational state transfer (REST)
- ASP.NET REST APIs with .NET and C#

Hypertext Transfer Protocol (HTTP) enables communication between clients and servers through a request-response protocol.

If you are not familiar with HTTP, then please google:

- HTTP Methods

Your web service application can authenticate logged-in users and set up[JSON Web Tokens (JWT)](https://jwt.io/introduction)Bearer tokens to securely authorize and restrict API access.

Read about the importance of[API Security](https://www.freecodecamp.org/news/authenticate-and-authorize-apis-in-dotnet5/).

##### Javascript, Python, and C# Console Examples

You will find examples scattered throughout the help. To get started with authenticating users, authorizing access, and using the GET and POST HTTP methods, follow the examples in[api/{vaultName}/authenticate](PDM%20Pro%20API_ws~r-api-{vaultName}-authenticate~o-HttpPost.html).

##### Install and Enable CORS

If you use browser-based programming languages like Java, PHP, Javascript, Python, NodeJs etc., you need CORS. The CORS extension can be downloaded and installed from Microsoft and enabled in IIS by editing the WebAPI**web.config**file as follows:

1. Go to**https://www.iis.net/downloads/microsoft/iis-cors-module**. Download and install the CORS module.
2. Navigate to the PDM Pro Web API installation location (e.g.,**C:\inetpub\wwwroot\SOLIDWORKSPDM\WebApi**).
3. Open**web.config**in any text editor with Administrator privileges (Notepad or Notepad++, for example).
4. Add the following lines to the <configuration><system.webServer> section:
<cors enabled='true'>
<add origin='*'>
<allowHeaders allowAllRequestedHeaders='true' />
<allowMethods>
<add method='GET' />
<add method='POST' />
<add method='PUT' />
<add method='DELETE' />
</allowMethods>
</add>
</cors>

The <system.webServer> section should look like this:

<system.webServer>
<security>
<requestFiltering>
<requestLimits maxAllowedContentLength='4294967295' />
</requestFiltering>
</security>
<handlers>
<remove name='ExtensionlessUrlHandler-Integrated-4.0' />
<remove name='OPTIONSVerbHandler' />
<remove name='TRACEVerbHandler' />
<add name='Owin' verb=' path='*' type='Microsoft.Owin.Host.SystemWeb.OwinHttpHandler, Microsoft.Owin.Host.SystemWeb' />
<add name='ExtensionlessUrlHandler-Integrated-4.0' path='*.' verb='*' type='System.Web.Handlers.TransferRequestHandler' preCondition='integratedMode,runtimeVersionv4.0' />
</handlers>
<cors enabled='true'>
<add origin='*'>
<allowHeaders allowAllRequestedHeaders='true' />
<allowMethods>
<add method='GET' />
<add method='POST' />
<add method='PUT' />
<add method='DELETE' />
</allowMethods>
</add>
</cors>
</system.webServer>

5. Save**web.config**.

6. Open the IIS Manager.

7. Stop the SWPDMWebAPI site.

8. Stop the SOLIDWORKS PDM WebAPI application pool.

9. Restart the SOLIDWORKS PDM WebAPI application pool.

10. Restart the SWPDMWebAPI site.
