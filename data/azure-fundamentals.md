# Azure Fundamentals: Essential Terms & Concepts

> A comprehensive guide to Microsoft Azure terminology with practical examples and explanations.

---

## Table of Contents

1. [Core Infrastructure Concepts](#core-infrastructure-concepts)
2. [Computing and Networking](#computing-and-networking)
3. [Storage and Databases](#storage-and-databases)
4. [Identity and Security](#identity-and-security)
5. [Common Operational Terms](#common-operational-terms)

---

## Core Infrastructure Concepts

### Azure Subscription

**Definition:** A logical unit of Azure services linked to an Azure account, used for billing and resource management.

**Description:** An Azure Subscription is essentially your "membership card" to use Azure services. When you create resources like virtual machines or databases, they must belong to a subscription. The subscription tracks everything you use and generates a monthly bill. Large companies often have multiple subscriptions to separate costs between departments (e.g., IT vs Marketing), environments (Production vs Development), or projects. Each subscription has spending limits you can set, and you can assign different payment methods to different subscriptions. Without a subscription, you cannot create any Azure resources.

Think of an Azure Subscription as your **contract with Microsoft** — it determines:
- What services you can use
- How you're billed
- Your spending limits

#### Example Scenario

```
Company: Contoso Ltd.
├── Subscription: "Production" (Pay-as-you-go)
│   ├── All production workloads
│   └── Billed to finance department
│
├── Subscription: "Development" (Dev/Test pricing)
│   ├── Development and testing environments
│   └── Billed to engineering budget
│
└── Subscription: "Sandbox" (Free tier)
    └── Experimentation and learning
```

#### Key Points
- One Azure account can have **multiple subscriptions**
- Each subscription has its own **billing cycle**
- Subscriptions help with **cost management** and **organizational boundaries**

---

### Azure Resource Group

**Definition:** A container that holds related resources for an Azure solution.

**Description:** A Resource Group is a logical container where you place Azure resources that work together. Imagine building a web application — you need a web server, a database, and storage for files. Instead of having these scattered randomly, you put them all in one Resource Group called "my-webapp". This makes management simple: you can see all related resources together, apply the same security settings to all of them, monitor their costs as a unit, and when the project ends, delete everything at once. Every Azure resource MUST belong to exactly one Resource Group. Resource Groups themselves are free — you only pay for the resources inside them.

A Resource Group is like a **folder** that organizes your Azure resources. All resources in a group share the same lifecycle — they're deployed, updated, and deleted together.

#### Example Scenario

```
Resource Group: "rg-ecommerce-prod"
├── Virtual Machine: "vm-webserver-01"
├── Virtual Machine: "vm-webserver-02"
├── Azure SQL Database: "sql-products-db"
├── Storage Account: "stoecommerceassets"
├── Load Balancer: "lb-ecommerce-frontend"
└── Virtual Network: "vnet-ecommerce"
```

#### Best Practices

| Practice | Example |
|----------|---------|
| Group by lifecycle | All resources for one app in one group |
| Use naming conventions | `rg-<project>-<environment>` |
| Apply tags for tracking | `environment: production`, `cost-center: marketing` |

#### Real-World Analogy
> Imagine you're moving houses. You pack kitchen items in one box, bedroom items in another. Resource Groups work the same way — related items stay together, making it easy to manage, move, or delete them as a unit.

---

### Azure Region

**Definition:** A set of datacenters deployed within a latency-defined perimeter, connected through a dedicated regional low-latency network.

**Description:** An Azure Region is a physical location in the world where Microsoft has built one or more datacenters. When you create a resource, you choose which region to put it in. This choice matters for three main reasons: (1) Speed — if your users are in Europe, put your app in a European region so data travels shorter distances; (2) Legal compliance — some laws require data to stay within certain countries (like GDPR in Europe); (3) Cost — prices vary between regions. Each region is isolated from others, so if one region has problems, others keep running. Some regions are "paired" with another nearby region for disaster recovery. Not all Azure services are available in all regions, so always check availability first.

Azure has **60+ regions** worldwide, more than any other cloud provider.

#### Example Regions

| Region Name | Location | Common Use Case |
|-------------|----------|-----------------|
| `westeurope` | Netherlands | European customers |
| `northeurope` | Ireland | EU data residency |
| `eastus` | Virginia, USA | North American users |
| `southeastasia` | Singapore | Asia-Pacific market |

#### Why Regions Matter

1. **Latency** — Deploy closer to users for faster response times
2. **Data Residency** — Meet legal requirements (GDPR, etc.)
3. **Pricing** — Costs vary by region
4. **Service Availability** — Not all services available in all regions

#### Example: Multi-Region Deployment

```
Global E-commerce Platform
├── Primary: West Europe (Netherlands)
│   ├── Main database (read/write)
│   └── European users
│
├── Secondary: East US (Virginia)
│   ├── Read replica
│   └── American users
│
└── Tertiary: Southeast Asia (Singapore)
    ├── Read replica
    └── Asian users
```

---

### Availability Set

**Definition:** A logical grouping of VMs that ensures redundancy and availability within a datacenter.

**Description:** An Availability Set is Azure's way of protecting your application from hardware failures and planned maintenance. When you put multiple VMs in an Availability Set, Azure automatically spreads them across different physical server racks (called Fault Domains) and different maintenance schedules (called Update Domains). This means if one rack loses power or needs maintenance, your other VMs keep running on different racks. Think of it like not putting all your eggs in one basket. For example, if you have 4 web servers in an Availability Set, Azure ensures they're on at least 2 different racks — so a single hardware failure never takes down all 4 servers at once. Availability Sets are free; you only pay for the VMs inside them.

Availability Sets protect against **hardware failures** by distributing VMs across:
- **Fault Domains (FD)** — Separate physical racks with independent power/network
- **Update Domains (UD)** — Groups that restart separately during maintenance

#### Visual Representation

```
Availability Set: "as-webservers"
┌─────────────────────────────────────────────────────────┐
│                                                         │
│  Fault Domain 0          Fault Domain 1                 │
│  ┌─────────────┐         ┌─────────────┐               │
│  │ Rack A      │         │ Rack B      │               │
│  │ ┌─────────┐ │         │ ┌─────────┐ │               │
│  │ │  VM-01  │ │         │ │  VM-02  │ │               │
│  │ └─────────┘ │         │ └─────────┘ │               │
│  │ ┌─────────┐ │         │ ┌─────────┐ │               │
│  │ │  VM-03  │ │         │ │  VM-04  │ │               │
│  │ └─────────┘ │         │ └─────────┘ │               │
│  └─────────────┘         └─────────────┘               │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

#### SLA Impact

| Configuration | SLA |
|---------------|-----|
| Single VM (Premium SSD) | 99.9% |
| Availability Set | 99.95% |
| Availability Zones | 99.99% |

---

### Azure Resource Manager (ARM)

**Definition:** The deployment and management service for Azure that provides a consistent management layer.

**Description:** Azure Resource Manager is the gateway through which ALL interactions with Azure pass. Whether you click a button in the Azure Portal, run a command in PowerShell, or make an API call, your request goes through ARM. ARM handles authentication (are you who you say you are?), authorization (are you allowed to do this?), and then sends your request to the appropriate Azure service. ARM also enables "Infrastructure as Code" through ARM Templates (now called Bicep) — JSON files that describe what resources you want. You can save these templates and reuse them to create identical environments repeatedly. This ensures consistency: your development, testing, and production environments can be exactly the same.

ARM is the **"brain"** of Azure — every action you take (portal, CLI, PowerShell, API) goes through ARM.

#### How ARM Works

```
┌──────────────────────────────────────────────────────────┐
│                    Your Request                          │
│   (Portal / CLI / PowerShell / SDK / REST API)          │
└─────────────────────────┬────────────────────────────────┘
                          │
                          ▼
┌──────────────────────────────────────────────────────────┐
│              Azure Resource Manager (ARM)                │
│                                                          │
│  • Authentication & Authorization                        │
│  • Request validation                                    │
│  • Resource orchestration                                │
└─────────────────────────┬────────────────────────────────┘
                          │
                          ▼
┌──────────────────────────────────────────────────────────┐
│              Azure Resource Providers                    │
│                                                          │
│  Microsoft.Compute  │  Microsoft.Storage  │  Microsoft.Sql
└──────────────────────────────────────────────────────────┘
```

#### ARM Templates (Infrastructure as Code)

```json
{
  "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",
  "contentVersion": "1.0.0.0",
  "resources": [
    {
      "type": "Microsoft.Storage/storageAccounts",
      "apiVersion": "2021-02-01",
      "name": "mystorageaccount",
      "location": "westeurope",
      "sku": {
        "name": "Standard_LRS"
      },
      "kind": "StorageV2"
    }
  ]
}
```

#### Benefits of ARM
- ✅ **Declarative syntax** — Define *what* you want, not *how*
- ✅ **Repeatable deployments** — Same template, same result
- ✅ **Dependency management** — ARM deploys resources in correct order
- ✅ **Role-based access control** — Applied across all resources
- ✅ **Tagging** — Organize and track resources

---

## Computing and Networking

### Virtual Machines (VMs)

**Definition:** IaaS-based, on-demand compute resources that give you full control over the operating system and software.

**Description:** A Virtual Machine is a complete computer running in Azure's datacenter that you control remotely. You choose the operating system (Windows, Linux, etc.), the size (how many CPUs, how much RAM), and what software to install. It's called "Infrastructure as a Service" (IaaS) because Azure provides the infrastructure (physical servers, networking, storage), but YOU manage everything inside the VM — installing updates, configuring software, handling security patches. VMs are perfect when you need full control or when migrating existing applications to the cloud without changing them. You pay by the minute/hour while the VM is running, and you can stop it to save money when not needed. Each VM also needs storage (for its disk) and networking, which may have additional costs.

VMs are like **renting a computer in the cloud** — you choose the OS, install software, and manage everything yourself.

#### VM Size Examples

| Size | vCPUs | Memory | Use Case |
|------|-------|--------|----------|
| B1s | 1 | 1 GB | Dev/Test, low traffic |
| D4s_v3 | 4 | 16 GB | General purpose workloads |
| E8s_v3 | 8 | 64 GB | Memory-intensive (databases) |
| NC6 | 6 | 56 GB | GPU compute (ML/AI) |

#### Example: Creating a VM (Azure CLI)

```bash
# Create a resource group
az group create --name rg-demo --location westeurope

# Create a virtual machine
az vm create \
  --resource-group rg-demo \
  --name vm-webserver \
  --image Ubuntu2204 \
  --size Standard_B2s \
  --admin-username azureuser \
  --generate-ssh-keys
```

#### When to Use VMs
- ✅ Lift-and-shift migrations
- ✅ Full control over OS needed
- ✅ Running legacy applications
- ✅ Custom software requirements

---

### App Service

**Definition:** A fully managed PaaS offering for hosting web applications, REST APIs, and mobile backends.

**Description:** App Service is Azure's fully managed platform for running web applications. Unlike VMs where you manage everything, with App Service you just upload your code and Azure handles the rest — the operating system, security patches, load balancing, and scaling. It supports multiple programming languages (Node.js, Python, .NET, Java, PHP, Ruby) and can pull code directly from GitHub for automatic deployments. You pay for an "App Service Plan" which determines how much CPU/RAM you get and features available. Multiple apps can share one plan to save costs. App Service includes built-in features like custom domains, SSL certificates, authentication, and deployment slots (for testing new versions before going live). It's ideal for web apps, APIs, and backends where you want to focus purely on coding.

App Service lets you **focus on code, not infrastructure**. Azure handles scaling, patching, and maintenance.

#### Comparison: VMs vs App Service

| Aspect | Virtual Machine | App Service |
|--------|-----------------|-------------|
| Control | Full OS access | Application level only |
| Maintenance | You patch/update | Azure handles it |
| Scaling | Manual or scripts | Built-in auto-scale |
| Cost | Pay for running VM | Pay for App Service Plan |
| Deployment | Manual or CI/CD | Git, GitHub Actions, Azure DevOps |

#### App Service Plans (Tiers)

```
Free (F1)           → Learning, testing
├── Shared (D1)     → Low-traffic sites
├── Basic (B1-B3)   → Dev/Test environments
├── Standard (S1-S3) → Production workloads
├── Premium (P1-P3)  → Enhanced performance
└── Isolated        → High security/compliance
```

#### Example: Deploy a Web App

```bash
# Create App Service Plan
az appservice plan create \
  --name plan-webapp \
  --resource-group rg-demo \
  --sku S1 \
  --is-linux

# Create Web App
az webapp create \
  --name myuniquewebapp \
  --resource-group rg-demo \
  --plan plan-webapp \
  --runtime "NODE:18-lts"

# Deploy from GitHub
az webapp deployment source config \
  --name myuniquewebapp \
  --resource-group rg-demo \
  --repo-url https://github.com/user/repo \
  --branch main
```

---

### Azure Virtual Network (VNet)

**Definition:** Enables Azure resources to securely communicate with each other, the internet, and on-premises networks.

**Description:** A Virtual Network is your own isolated, private network inside Azure. Just like a company has an internal network where computers can talk to each other securely, a VNet does the same for your Azure resources. You define IP address ranges (like 10.0.0.0/16), create subnets to organize resources (web servers in one subnet, databases in another), and control traffic flow with security rules. Resources in a VNet can communicate with each other by default, but you control what can reach the internet and what can't. VNets can also connect to your on-premises datacenter via VPN or ExpressRoute, creating a hybrid network. VNets are free — you only pay for certain features like VPN Gateways or public IP addresses.

A VNet is your **private network in Azure** — you control IP addresses, subnets, routing, and security.

#### VNet Architecture Example

```
Virtual Network: vnet-production (10.0.0.0/16)
│
├── Subnet: snet-web (10.0.1.0/24)
│   ├── vm-web-01 (10.0.1.4)
│   ├── vm-web-02 (10.0.1.5)
│   └── Network Security Group: nsg-web
│       └── Allow HTTP/HTTPS from internet
│
├── Subnet: snet-app (10.0.2.0/24)
│   ├── vm-app-01 (10.0.2.4)
│   └── Network Security Group: nsg-app
│       └── Allow traffic from snet-web only
│
├── Subnet: snet-db (10.0.3.0/24)
│   ├── Azure SQL (Private Endpoint)
│   └── Network Security Group: nsg-db
│       └── Allow traffic from snet-app only
│
└── Gateway Subnet (10.0.255.0/27)
    └── VPN Gateway → On-premises network
```

#### Key VNet Features

| Feature | Description |
|---------|-------------|
| **Subnets** | Divide VNet into smaller segments |
| **NSG** | Network Security Groups filter traffic |
| **Peering** | Connect VNets together |
| **VPN Gateway** | Connect to on-premises |
| **Private Endpoints** | Access PaaS services privately |

---

### Azure Load Balancer

**Definition:** Distributes incoming network traffic across multiple backend servers to ensure high availability.

**Description:** A Load Balancer sits in front of multiple servers and distributes incoming requests among them. Imagine a popular website with millions of visitors — one server can't handle all that traffic. Instead, you have 10 servers, and the Load Balancer spreads visitors across all 10. If one server fails, the Load Balancer detects this (using "health probes" — regular checks to see if servers are responding) and stops sending traffic to it. Users never notice the failure. Azure offers two types: Layer 4 (basic TCP/UDP traffic distribution) and Layer 7 Application Gateway (understands HTTP, can route based on URL paths, handles SSL). Load Balancers are essential for building reliable, scalable applications that can handle high traffic and survive server failures.

#### Load Balancer Types

| Type | Layer | Use Case |
|------|-------|----------|
| **Basic** | Layer 4 (TCP/UDP) | Simple scenarios, free |
| **Standard** | Layer 4 (TCP/UDP) | Production, zone-redundant |
| **Application Gateway** | Layer 7 (HTTP/HTTPS) | Web apps, URL-based routing |

#### How It Works

```
                    Internet
                        │
                        ▼
              ┌─────────────────┐
              │  Load Balancer  │
              │  Public IP:     │
              │  52.166.XXX.XXX │
              └────────┬────────┘
                       │
         ┌─────────────┼─────────────┐
         │             │             │
         ▼             ▼             ▼
    ┌─────────┐   ┌─────────┐   ┌─────────┐
    │  VM-01  │   │  VM-02  │   │  VM-03  │
    │ 10.0.1.4│   │ 10.0.1.5│   │ 10.0.1.6│
    └─────────┘   └─────────┘   └─────────┘
```

#### Health Probes

Load Balancer checks backend health before routing traffic:

```
Health Probe Configuration:
├── Protocol: HTTP
├── Port: 80
├── Path: /health
├── Interval: 15 seconds
└── Unhealthy threshold: 2 failures
```

---

## Storage and Databases

### Azure Blob Storage

**Definition:** Object storage solution optimized for storing massive amounts of unstructured data (images, videos, documents, backups).

**Description:** Blob Storage is Azure's service for storing large amounts of unstructured data — files that don't fit neatly into databases like images, videos, PDFs, backups, and logs. "Blob" stands for Binary Large Object. It's incredibly scalable (petabytes of data) and durable (data is replicated multiple times). You create a Storage Account, then create "containers" (like folders), and upload files (blobs) into them. Blob Storage has different "access tiers": Hot (frequently accessed, higher storage cost, lower access cost), Cool (infrequent access), Cold (rare access), and Archive (long-term backup, cheapest storage but slow retrieval). You can set lifecycle policies to automatically move old files to cheaper tiers. Blobs can be accessed via URLs, making them perfect for hosting images on websites or storing application data.

#### Storage Account Hierarchy

```
Storage Account: stproductiondata
│
├── Container: images
│   ├── product-001.jpg
│   ├── product-002.jpg
│   └── banners/
│       └── hero-banner.png
│
├── Container: documents
│   ├── invoice-2024-001.pdf
│   └── contracts/
│       └── agreement.docx
│
└── Container: backups
    └── db-backup-2024-01-15.bak
```

#### Access Tiers

| Tier | Use Case | Access Cost | Storage Cost |
|------|----------|-------------|--------------|
| **Hot** | Frequently accessed data | Lowest | Highest |
| **Cool** | Infrequent access (30+ days) | Medium | Medium |
| **Cold** | Rare access (90+ days) | Higher | Lower |
| **Archive** | Long-term backup (180+ days) | Highest | Lowest |

#### Example: Upload to Blob Storage

```bash
# Create storage account
az storage account create \
  --name stmyuniqueaccount \
  --resource-group rg-demo \
  --location westeurope \
  --sku Standard_LRS

# Create container
az storage container create \
  --name images \
  --account-name stmyuniqueaccount

# Upload file
az storage blob upload \
  --account-name stmyuniqueaccount \
  --container-name images \
  --name photo.jpg \
  --file ./local-photo.jpg
```

---

### Azure SQL Database

**Definition:** A fully managed relational database service based on the latest stable version of Microsoft SQL Server.

**Description:** Azure SQL Database is a fully managed relational database in the cloud. "Fully managed" means Microsoft handles all the hard work: hardware setup, patching, backups, high availability, and security updates. You just create a database, connect your application, and start storing data. It uses the familiar SQL Server engine, so existing SQL Server skills and code work with minimal changes. Built-in features include automatic backups (restore to any point in the last 35 days), threat detection (alerts for suspicious activity like SQL injection attacks), automatic performance tuning (AI analyzes queries and suggests indexes), and geo-replication (copies in other regions for disaster recovery). You pay based on compute power (DTUs or vCores) and storage used. It's ideal for applications needing a reliable, scalable relational database without database administration overhead.

#### Service Tiers

| Tier | DTU/vCore | Use Case |
|------|-----------|----------|
| **Basic** | 5 DTU | Light workloads, dev/test |
| **Standard** | 10-3000 DTU | Most production workloads |
| **Premium** | 125-4000 DTU | High IOPS, mission-critical |
| **Hyperscale** | Up to 100 vCores | Large databases (up to 100 TB) |

#### Built-in Features

- ✅ **Automatic backups** — Point-in-time restore up to 35 days
- ✅ **Geo-replication** — Read replicas in other regions
- ✅ **Automatic tuning** — AI-driven performance optimization
- ✅ **Threat detection** — SQL injection protection
- ✅ **Encryption** — Data encrypted at rest and in transit

#### Example: Connection String

```csharp
// C# connection string
string connectionString = 
  "Server=tcp:myserver.database.windows.net,1433;" +
  "Database=mydb;" +
  "User ID=myadmin;" +
  "Password=MyP@ssw0rd!;" +
  "Encrypt=True;" +
  "TrustServerCertificate=False;";
```

---

### Cosmos DB

**Definition:** A globally distributed, multi-model database service designed for low latency and massive scale.

**Description:** Cosmos DB is Azure's premium globally distributed database designed for applications that need lightning-fast responses anywhere in the world. Unlike traditional databases in one location, Cosmos DB can replicate your data across multiple Azure regions simultaneously. A user in Tokyo reads from a nearby copy, while a user in London reads from their nearby copy — both get responses in single-digit milliseconds. It supports multiple data models through different APIs: document (JSON), key-value, graph, and column-family. This flexibility means you can use it for various use cases without learning entirely new database systems. You choose your consistency level (from "Strong" — always latest data, to "Eventual" — faster but might read slightly old data). Cosmos DB guarantees 99.999% availability and is priced based on storage and "Request Units" (RU) — a measure of database operations.

#### Supported APIs (Data Models)

| API | Data Model | Use Case |
|-----|------------|----------|
| **NoSQL** | Document (JSON) | Modern apps, flexible schema |
| **MongoDB** | Document (BSON) | MongoDB migrations |
| **Cassandra** | Wide-column | Time-series, IoT |
| **Gremlin** | Graph | Social networks, recommendations |
| **Table** | Key-value | Simple lookups |

#### Global Distribution Example

```
Cosmos DB Account: cosmos-globalapp
│
├── Write Region: West Europe (Primary)
│   └── Latency: <10ms for EU users
│
├── Read Region: East US
│   └── Latency: <10ms for US users
│
└── Read Region: Southeast Asia
    └── Latency: <10ms for Asian users

Automatic failover if primary region goes down!
```

#### Consistency Levels

```
Strong ─────────────────────────────────────► Eventual
  │                                              │
  │  • Strong: Latest data, highest latency     │
  │  • Bounded Staleness: Guaranteed lag        │
  │  • Session: Consistent within session       │
  │  • Consistent Prefix: Ordered reads         │
  │  • Eventual: Fastest, may read old data     │
  │                                              │
  └──────────────────────────────────────────────┘
```

---

## Identity and Security

### Azure Active Directory (Azure AD / Entra ID)

**Definition:** Microsoft's cloud-based identity and access management service for signing in and accessing resources.

**Description:** Azure Active Directory (now called Microsoft Entra ID) is Azure's identity service — it manages WHO can access WHAT. Think of it as the bouncer and ID checker for all your cloud resources and applications. When employees log into Microsoft 365, Azure Portal, or your company's custom apps, Azure AD verifies their identity. It stores user accounts, passwords (encrypted), and group memberships. Key features include Single Sign-On (SSO) — log in once, access all your apps; Multi-Factor Authentication (MFA) — require a phone code in addition to password; Conditional Access — block logins from unusual locations or require extra verification. Azure AD can sync with on-premises Active Directory, so employees use the same credentials everywhere. Every Azure subscription is automatically associated with an Azure AD tenant.

> **Note:** Azure AD has been renamed to **Microsoft Entra ID** (2023), but the functionality remains the same.

#### What Azure AD Manages

```
Microsoft Entra ID
│
├── Users
│   ├── Employees (synced from on-prem AD)
│   ├── Guest users (B2B collaboration)
│   └── Service accounts
│
├── Groups
│   ├── Security groups
│   └── Microsoft 365 groups
│
├── Applications
│   ├── Enterprise apps (SaaS)
│   ├── Custom apps
│   └── Microsoft 365
│
└── Devices
    ├── Azure AD joined
    ├── Azure AD registered
    └── Hybrid Azure AD joined
```

#### Key Features

| Feature | Description |
|---------|-------------|
| **Single Sign-On (SSO)** | One login for all apps |
| **Multi-Factor Authentication (MFA)** | Extra security layer |
| **Conditional Access** | Policies based on conditions |
| **Privileged Identity Management** | Just-in-time admin access |
| **Identity Protection** | Risk-based policies |

#### Conditional Access Example

```
Policy: "Require MFA for admins"
│
├── Assignments
│   ├── Users: Global Administrators
│   ├── Apps: All cloud apps
│   └── Conditions: Any location
│
└── Access Controls
    └── Grant: Require MFA
```

---

### Role-Based Access Control (RBAC)

**Definition:** Manages who has access to Azure resources, what they can do with those resources, and what areas they can access.

**Description:** RBAC is Azure's authorization system that controls what users can DO with resources. While Azure AD handles "who are you?" (authentication), RBAC handles "what are you allowed to do?" (authorization). It works by assigning "roles" to users at specific "scopes". A role is a collection of permissions (like "can read", "can create", "can delete"). A scope is where those permissions apply (entire subscription, a resource group, or a single resource). For example: "Sarah has the Contributor role on the Production resource group" means Sarah can create, modify, and delete any resource in that group, but not in other groups. Built-in roles include Owner (full control), Contributor (full control except permissions), Reader (view only), and many specialized roles. You can also create custom roles. Always follow "least privilege" — give only the permissions needed.

#### RBAC Components

```
Who?                What?                  Where?
(Security           (Role                  (Scope)
Principal)          Definition)
    │                   │                     │
    ▼                   ▼                     ▼
┌─────────┐       ┌───────────┐       ┌──────────────┐
│  User   │  ──►  │   Owner   │  ──►  │ Subscription │
│  Group  │       │Contributor│       │Resource Group│
│  App    │       │  Reader   │       │   Resource   │
└─────────┘       └───────────┘       └──────────────┘
                         │
                         ▼
               ┌─────────────────┐
               │ Role Assignment │
               │                 │
               │ "John has       │
               │  Contributor    │
               │  access to      │
               │  rg-production" │
               └─────────────────┘
```

#### Built-in Roles

| Role | Permissions |
|------|-------------|
| **Owner** | Full access + can assign roles to others |
| **Contributor** | Full access, cannot assign roles |
| **Reader** | View only, no changes |
| **User Access Administrator** | Manage user access only |

#### Example: Assign Role (Azure CLI)

```bash
# Assign Contributor role to a user for a resource group
az role assignment create \
  --assignee user@company.com \
  --role "Contributor" \
  --scope /subscriptions/{sub-id}/resourceGroups/rg-production
```

#### Principle of Least Privilege

> Always grant the **minimum permissions** needed to perform a task.

```
❌ Bad:  Give everyone Owner access "just in case"
✅ Good: Developers get Contributor on dev, Reader on prod
✅ Good: DBAs get SQL DB Contributor on databases only
```

---

## Common Operational Terms

### Scaling Up/Down (Vertical Scaling)

**Definition:** Increasing or decreasing the power (CPU, RAM, storage) of existing resources.

**Description:** Vertical scaling means making your existing machine more powerful (scaling UP) or less powerful (scaling DOWN). Imagine your database server is struggling because it has only 4GB RAM. Instead of adding more servers, you upgrade to 16GB RAM — that's scaling up. Later, during quiet periods, you downgrade back to 4GB to save money — that's scaling down. In Azure, this means changing your VM size or database tier. The advantage is simplicity: no code changes, just a bigger machine. The disadvantages are: (1) there's a maximum size limit — you can only get so big; (2) usually requires a restart, causing brief downtime; (3) it's still one machine, so if it fails, everything fails. Vertical scaling works well for databases and stateful applications that can't easily run on multiple machines.

#### Visual Representation

```
Scaling UP (More Power)
┌─────────┐      ┌─────────────┐      ┌───────────────────┐
│  B1s    │  ──► │    D2s      │  ──► │       D4s         │
│ 1 vCPU  │      │  2 vCPUs    │      │     4 vCPUs       │
│  1 GB   │      │   8 GB      │      │      16 GB        │
└─────────┘      └─────────────┘      └───────────────────┘

Scaling DOWN (Less Power)
┌───────────────────┐      ┌─────────────┐      ┌─────────┐
│       D4s         │  ──► │    D2s      │  ──► │  B1s    │
│     4 vCPUs       │      │  2 vCPUs    │      │ 1 vCPU  │
│      16 GB        │      │   8 GB      │      │  1 GB   │
└───────────────────┘      └─────────────┘      └─────────┘
```

#### When to Use Vertical Scaling

| Scenario | Action |
|----------|--------|
| Database needs more memory | Scale UP to larger VM size |
| App runs slow during peak hours | Scale UP temporarily |
| Over-provisioned during off-hours | Scale DOWN to save costs |
| Hitting CPU limits | Scale UP to more cores |

#### Limitations
- ⚠️ **Downtime required** — Usually requires restart
- ⚠️ **Upper limit** — Can only scale up to largest available size
- ⚠️ **Single point of failure** — Still one instance

---

### Scaling Out/In (Horizontal Scaling)

**Definition:** Adding or removing instances of resources to handle varying loads.

**Description:** Horizontal scaling means adding MORE machines (scaling OUT) or removing machines (scaling IN) based on demand. Instead of making one server bigger, you add more servers and spread the work. When traffic increases, you add servers; when it decreases, you remove them. This approach has major advantages: (1) virtually unlimited scaling — just keep adding machines; (2) no downtime — new machines join while existing ones keep running; (3) fault tolerance — if one machine fails, others continue working. The challenge is your application must be designed for it — typically "stateless" apps where any server can handle any request. In Azure, services like Virtual Machine Scale Sets and App Service auto-scaling handle this automatically based on rules you define (e.g., "add 2 VMs when CPU exceeds 70%"). This is the preferred approach for modern web applications.

#### Visual Representation

```
Scaling OUT (More Instances)
┌─────────┐              ┌─────────┐ ┌─────────┐ ┌─────────┐
│  VM-01  │          ──► │  VM-01  │ │  VM-02  │ │  VM-03  │
└─────────┘              └─────────┘ └─────────┘ └─────────┘

Scaling IN (Fewer Instances)
┌─────────┐ ┌─────────┐ ┌─────────┐              ┌─────────┐
│  VM-01  │ │  VM-02  │ │  VM-03  │          ──► │  VM-01  │
└─────────┘ └─────────┘ └─────────┘              └─────────┘
```

#### Auto-Scale Rules Example

```
Auto-scale Configuration: "scale-webapp"
│
├── Default instances: 2
├── Minimum instances: 1
├── Maximum instances: 10
│
├── Scale OUT Rule:
│   └── When CPU > 70% for 10 minutes
│       → Add 2 instances
│
└── Scale IN Rule:
    └── When CPU < 30% for 10 minutes
        → Remove 1 instance
```

#### Comparison: Vertical vs Horizontal

| Aspect | Vertical (Up/Down) | Horizontal (Out/In) |
|--------|-------------------|---------------------|
| Method | Bigger/smaller machine | More/fewer machines |
| Downtime | Usually required | No downtime |
| Cost | Pay for larger size | Pay per instance |
| Limit | Hardware maximum | Virtually unlimited |
| Complexity | Simple | Requires load balancing |
| Best for | Databases, legacy apps | Stateless web apps, APIs |

---

### Serverless Computing

**Definition:** A cloud execution model where the provider dynamically manages resource allocation. You pay only for actual compute time used.

**Description:** Serverless computing lets you run code without thinking about servers at all. You write a function (small piece of code), upload it to Azure, and define what "triggers" it (HTTP request, timer, file upload, message queue, etc.). When the trigger occurs, Azure automatically spins up the infrastructure, runs your code, and shuts it down. You pay ONLY for the milliseconds your code actually runs — if nobody calls your function, you pay nothing. Azure handles all scaling automatically: whether you get 1 request or 1 million, it just works. The main service is Azure Functions. Limitations include: execution time limits (typically 5-10 minutes max), "cold starts" (first request after idle time is slower), and stateless nature (functions don't remember previous executions). Perfect for event-driven tasks, APIs with variable traffic, scheduled jobs, and glue code connecting services.

#### Serverless Services in Azure

| Service | Use Case |
|---------|----------|
| **Azure Functions** | Event-driven code execution |
| **Logic Apps** | Workflow automation |
| **Event Grid** | Event routing |
| **Azure Container Apps** | Containerized microservices |

#### Azure Functions Example

```javascript
// Azure Function: HTTP Trigger
module.exports = async function (context, req) {
    const name = req.query.name || req.body?.name || "World";
    
    context.res = {
        status: 200,
        body: `Hello, ${name}!`
    };
};
```

#### Serverless vs Traditional

```
Traditional (Always Running)
┌────────────────────────────────────────────────┐
│ ████████████████████████████████████████████ │ ← Paying 24/7
└────────────────────────────────────────────────┘

Serverless (Pay Per Use)
┌────────────────────────────────────────────────┐
│     ██    ████   ██     ███████    ██         │ ← Pay only when
└────────────────────────────────────────────────┘   function runs
```

#### When to Use Serverless

✅ **Good fit:**
- Event-driven processing
- Scheduled tasks (cron jobs)
- APIs with variable traffic
- Data processing pipelines
- Webhooks and integrations

❌ **Not ideal:**
- Long-running processes (>15 min)
- Applications needing persistent connections
- High-performance computing
- Stateful applications

---

## Quick Reference Card

```
┌─────────────────────────────────────────────────────────────┐
│                    AZURE HIERARCHY                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Azure Account (your login)                                 │
│       │                                                     │
│       └── Subscription (billing boundary)                   │
│               │                                             │
│               └── Resource Group (logical container)        │
│                       │                                     │
│                       └── Resources (VMs, DBs, etc.)        │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                    COMPUTE OPTIONS                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  More Control ◄─────────────────────────► Less Management   │
│                                                             │
│  VMs ──► Container ──► App Service ──► Functions            │
│  (IaaS)   Instances      (PaaS)       (Serverless)          │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                    SCALING SUMMARY                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Vertical (Up/Down): Bigger machine    [Database, Legacy]   │
│  Horizontal (Out/In): More machines    [Web apps, APIs]     │
│  Serverless: Auto-managed              [Events, Tasks]      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Summary

| Term | One-Line Summary |
|------|------------------|
| **Subscription** | Your billing account for Azure services |
| **Resource Group** | Folder to organize related resources |
| **Region** | Physical datacenter location |
| **Availability Set** | Keeps VMs running during failures |
| **ARM** | Azure's management and deployment engine |
| **Virtual Machine** | Your own server in the cloud (IaaS) |
| **App Service** | Managed web hosting (PaaS) |
| **VNet** | Private network in Azure |
| **Load Balancer** | Distributes traffic across servers |
| **Blob Storage** | Store files, images, backups |
| **Azure SQL** | Managed SQL Server database |
| **Cosmos DB** | Globally distributed NoSQL database |
| **Azure AD / Entra ID** | Identity and access management |
| **RBAC** | Control who can do what |
| **Vertical Scaling** | Bigger/smaller resources |
| **Horizontal Scaling** | More/fewer instances |
| **Serverless** | Pay only for what you use |

---

*Created for Azure fundamentals learning and RAG knowledge base*
