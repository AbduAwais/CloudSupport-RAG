/**
 * TypeScript types and interfaces for the RAG Chat API
 */

export interface ChatMessage {
  role: 'user' | 'assistant';
  content: string;
  timestamp: string;
  sources?: SourceDocument[];
}

export interface SourceDocument {
  source?: string;
  page?: number;
  [key: string]: any;
}

export interface ChatRequest {
  message: string;
  conversation_id?: string;
  system_prompt?: string;
}

export interface ChatResponse {
  conversation_id: string;
  user_message: string;
  assistant_message: string;
  sources: SourceDocument[];
  timestamp: string;
}

export interface Conversation {
  id: string;
  title?: string;
  messages: ChatMessage[];
  created_at: string;
  updated_at: string;
}

export interface PromptTemplate {
  id?: string;
  name: string;
  content: string;
  description?: string;
  created_at?: string;
  updated_at?: string;
}

export interface ApiError {
  detail?: string;
  message?: string;
}
